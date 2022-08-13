import os
import re
import time
import json
import base64
import requests
import websocket
from threading import Thread, Event

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QMessageBox

from consts import *

class Opcode:
    PING            = 'ping'
    RESULT          = 'result'
    CONNECTED       = 'connected'

class Client():
    '''
    This class is our middleman between us and atshop,
    and it handles everything related to websockets.
    '''

    def __init__(self, token):
        self.token = token

        self._response = Event()
        self._response_data = ''

        self._connected = Event()
        self._websocket = self.create_websocket()

        self.insert = pyqtSignal

        self.start()

    def create_websocket(self):
        return websocket.WebSocketApp(
            url=ROOT.format(
                token=self.token
            ),
            on_open=lambda ws: self.on_open(ws),
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_error=lambda ws, msg: self.on_error(ws, msg),
            on_close=lambda ws, close_code, close_msg: self.on_close(ws, close_code, close_msg)
        )

    def on_open(self, ws):
        pass

    def on_close(self, ws, close_code, close_msg):
        self.connected = False

    def on_error(self, ws, error):
        print(error)

    def on_message(self, ws, msg):
        if '42' in msg:
            response = json.loads('{' + msg.partition('{')[2][:-1])
            message = response.get('message')

            if message:
                if len(message) == 40:
                    Thread(target=self.heartbeat).start()
                    # Keeping the session alive

                    self._connected.set()

                    for item in message[::-1]:
                        data = self.parse_message(item)

                        self._response_data = [
                            data[0],
                            data[1],

                            data[2],
                            data[3],

                            response['room'],
                            data[4]
                        ]
                        self._response.set()

                else:
                    data = self.parse_message(message)

                    self._response_data = [
                        data[0],
                        data[1],

                        data[2],
                        data[3],

                        response['room'],

                        data[4]
                    ]
                    self._response.set()

        elif '44' in msg:
            self._connected.set()

            alert = QMessageBox()

            alert.setIcon(2)
            alert.setWindowTitle('Auth')
            alert.setText('Expired user token.')

            os._exit(
                alert.exec_()
            )

    def heartbeat(self):
        while True:
            self._websocket.send('2')
            # Ping message

            time.sleep(10)

    def parse_message(self, message):
        user = message['username']
        content = message['content']

        name = user.split('">')[-1].partition('</span></a>')[0]
        name = f'<span class="name">&nbsp;&nbsp;&nbsp;&nbsp;{name}</span>'

        items = list(
            filter(
                None,
                [
                    k if k in content else None
                    for k in next(os.walk('assets/images/items'), (None, None, []))[2]
                ]
            )
        )

        group = list(
            filter(
                None,
                [
                    v if k in user else None
                    for k, v in RANKS.items()
                ]
            )
        )
        group = group[0] if group else 'ffffff'

        ping = list(
            filter(
                None,
                [
                    [k, v] if k in content else None
                    for k, v in RANKS.items()
                ]
            )
        )
        ping = f'.{ping[0][0]} {{color: #{ping[0][1]}; text-decoration: none;}}' if ping else '* {color: #C0392B}' if message.get('private') else ''

        for smilie, path in SMILIES.items():
            if smilie in content:
                content = content.replace(smilie, f'<img style="width: 32px; height: 32px" src="{path}"/>')

        if 'https://static.cracked.io/' in content:
            paths = re.findall('https:\/\/static.cracked.io(.*?\")', content)

            for path in paths:
                path = path[:-1]

                image = base64.b64encode(
                    requests.get(
                        f'https://static.cracked.io{path}'
                    ).content
                ).decode('ascii')

                content = content.replace(f'src="https://static.cracked.io{path}"', f'src="data:image/png;base64,{image}" style="width: 32px; height: 32px"')

        # Parsing emojis & user items in the message

        if message.get('item'):
            image = base64.b64encode(
                requests.get(
                    message['item']
                ).content
            ).decode('ascii')

            name += f'  <img src="data:image/png;base64,{image}" width=14 height=14/></img>'

        # Username Items

        avatar = base64.b64encode(
            requests.get(
                message['avatar']
            ).content
        ).decode('ascii')

        name = f'<img class="avatar" src="data:image/png;base64,{avatar}" width=20 height=20/></img>' + name

        # Setting the users avatar

        return [
            name, # Username
            group, # Username Group

            content, # Message
            ping, # Ping colors inside of message

            True if len(message['content']) >= 135 else False # Word-wrap
        ]

    def start(self):
        Thread(
            target=self._websocket.run_forever,
            kwargs={
                'ping_interval': 15,
                'ping_timeout': 10
            }
        ).start()

        self._connected.wait()

        # Waiting for the websocket to connect to atshop
        # if we do not include this, our code will begin
        # executing before we want to. The result of this is
        # websocket._exceptions.WebSocketConnectionClosedException
