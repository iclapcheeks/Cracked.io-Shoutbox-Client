import os
import sys
import pickle

import PyQt5.sip
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, QPalette, QColor, QImage
from PyQt5.QtWidgets import (
                                QApplication, QMainWindow, QGridLayout,
                                QPushButton, QWidget, QVBoxLayout,
                                QLabel, QAbstractItemView, QAbstractScrollArea,
                                QTableWidget, QLineEdit, QFormLayout,
                                QTabWidget
                            )

from api import Client
from themes import theme

app = QApplication(sys.argv)
app.setPalette(theme)
app.setStyle('Fusion')
app.setAttribute(Qt.AA_UseHighDpiPixmaps)

class Message(QThread):
    new_signal = pyqtSignal(list)

    def run(self):
        while True:
            Window.client._response.wait()
            Window.client._response.clear()

            self.new_signal.emit(Window.client._response_data)

class Actions(QWidget):
    def __init__(self, Window):
        super().__init__()

        self.Window = Window

    def start_client(self):
        self.Window.start_btn.setEnabled(False)
        self.Window.client = Client(
            token=self.Window.token.text(),
        )

        self.Message = Message()
        self.Message.new_signal.connect(self.insert_row)
        self.Message.start()

    def resource(self, path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.abspath(
                os.path.join(
                    sys._MEIPASS,
                    './'
                ) + path
            )

        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                './'
            ) + path
        )

    def save_settings(self):
        with open(
            self.resource(
                'assets/configs/settings'
            ),
            'wb'
        ) as file:
            pickle.dump(
                self.Window.token.text(),
                file
            )

        self.Window.settings.hide()

        self.load_settings()

    def load_settings(self):
        try:
            with open(
                self.resource(
                    'assets/configs/settings'
                ),
                'rb'
            ) as file:
                data = pickle.load(file)

            self.Window.token.setText(data)

        except:
            try:
                os.remove('assets/configs/settings')
            except:
                pass

    def before_insert(self):
        vbar = self.Window.table.verticalScrollBar()
        self._scroll = vbar.value() == vbar.maximum()

    def after_insert(self):
        self.Window.table.scrollToBottom()

    @pyqtSlot(list)
    def insert_row(self, data):
        name = QLabel(f'<style>img {{vertical-align: top}} .name {{overflow: hidden; white-space: nowrap; color: #{data[1]}}}</style><div>{data[0]}</div>')
        content = QLabel(f'<style>p {{vertical-align: middle; color: #d1d1d1}} img {{vertical-align: middle}}{data[3]}</style><div><p>{data[2]}</p></div>')
        # Setting up the style of the row

        content.setTextInteractionFlags(Qt.TextBrowserInteraction)
        content.setOpenExternalLinks(True)
        # Making the links clickable

        table = self.Window.table_main if data[4] == 'main' else self.Window.table_market
        # Sending the message in the tab selected (main/market)

        row = table.rowCount()

        table.insertRow(row)

        if data[5]:
            table.setRowHeight(row, 50)
            content.setWordWrap(True)

        table.setCellWidget(row, 0, name)
        table.setCellWidget(row, 1, content)
        # Creating a new row and inserting the data into it

        table.selectRow(row)
        table.clearSelection()
        # Autoscrolling to the bottom

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.actions = Actions(self)

        self.setWindowTitle('Cracked.io Shoutbox by clap')
        self.setWindowIcon(
            QIcon(
                self.actions.resource('assets/images/components/favicon.png')
            )
        )

        self.shoutbox()
        self.settings()

        self.actions.load_settings()

    def shoutbox(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Main Window

        grid = QGridLayout()

        self.table_main = QTableWidget(0, 2)
        self.table_main.setColumnWidth(0, 135)
        self.table_main.setHorizontalHeaderLabels(['User', 'Message'])
        self.table_main.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_main.horizontalHeader().setStretchLastSection(True)
        self.table_main.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_main.setSortingEnabled(True)
        self.table_main.verticalHeader().hide()
        self.table_main.verticalHeader().setDefaultSectionSize(35)
        self.table_main.setStyleSheet('QTableWidget::item { margin-left: 5px }')

        # Main Table

        self.table_market = QTableWidget(0, 2)
        self.table_market.setHorizontalHeaderLabels(['User', 'Message'])
        self.table_market.setColumnWidth(0, 135)
        self.table_market.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_market.horizontalHeader().setStretchLastSection(True)
        self.table_market.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_market.setSortingEnabled(True)
        self.table_market.verticalHeader().hide()
        self.table_market.verticalHeader().setDefaultSectionSize(35)
        self.table_market.setStyleSheet('QTableWidget::item { margin-left: 5px }')

        # Marketplace Table

        self.start_btn = QPushButton(
            QIcon(
                self.actions.resource('assets/images/components/start.svg')
            ),
            '  Connect'
        )
        self.settings_btn = QPushButton(
            QIcon(
                self.actions.resource('assets/images/components/settings.svg')
            ),
            '  Settings'
        )

        self.start_btn.clicked.connect(lambda: self.actions.start_client())
        self.settings_btn.clicked.connect(lambda: self.settings.show() if not self.settings.isVisible() else self.settings.raise_())

        # Buttons

        self.chat = QLineEdit()
        self.chat.setPlaceholderText('Enter message...')

        self.send = QPushButton(
            QIcon(
                self.actions.resource('assets/images/components/send.png')
            ),
            ' Send'
        )
        self.send.clicked.connect(lambda: [self.client._websocket.send(f'42[2,{{"message":"{self.chat.text()}","room":"main"}}]' if not self.tabs.currentIndex() else f'42[2,{{"message":"{self.chat.text()}","room":"market"}}]'), self.chat.clear()])

        # Chat interaction

        self.options = QWidget()

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        layout = QFormLayout()

        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.settings_btn)
        vbox.setAlignment(Qt.AlignCenter)

        self.options.setLayout(vbox)

        # Options

        self.tabs = QTabWidget()
        self.tabs.addTab(self.table_main, 'Main')
        self.tabs.addTab(self.table_market, 'Marketplace')
        self.tabs.addTab(self.options, 'Options')

        # Tab Layout

        grid.addWidget(self.tabs, 2, 0, 1, 3)
        grid.addWidget(self.chat, 3, 0, 1, 2)
        grid.addWidget(self.send, 3, 2)

        widget.setLayout(grid)

        self.resize(1000, 350)
        self.show()

    def settings(self):
        self.settings = QMainWindow()
        self.settings.setWindowTitle('Settings')

        settings = QWidget()
        self.settings.setCentralWidget(settings)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        layout = QFormLayout()

        # Settings Window

        self.token = QLineEdit()
        layout.addRow(QLabel('Shoutbox Token:'), self.token)

        save_btn = QPushButton('Save')
        save_btn.clicked.connect(self.actions.save_settings)

        vbox.addLayout(layout)
        vbox.addWidget(save_btn)
        settings.setLayout(vbox)

        # Layout

        self.settings.resize(250, 50)

if __name__ == '__main__':
    Window = Window()

    os._exit(
        app.exec_()
    )
