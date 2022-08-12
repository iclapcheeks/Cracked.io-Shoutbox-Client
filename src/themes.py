from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap, QPalette, QColor

theme = QPalette()
theme.setColor(QPalette.Window, QColor(35, 39, 48))
theme.setColor(QPalette.WindowText, Qt.white)
theme.setColor(QPalette.Base, QColor(24, 27, 33))
theme.setColor(QPalette.AlternateBase, QColor(35, 39, 48))
theme.setColor(QPalette.ToolTipBase, Qt.white)
theme.setColor(QPalette.ToolTipText, Qt.white)
theme.setColor(QPalette.Text, Qt.white)
theme.setColor(QPalette.Button, QColor(35, 39, 48))
theme.setColor(QPalette.ButtonText, Qt.white)
theme.setColor(QPalette.BrightText, Qt.red)
theme.setColor(QPalette.Highlight, QColor(35, 41, 48))
theme.setColor(QPalette.HighlightedText, Qt.black)
theme.setColor(QPalette.Link, QColor(42, 130, 218))
theme.setColor(QPalette.LinkVisited, Qt.black)
