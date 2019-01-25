import sys
import threading
import time
import json

import requests
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMainWindow, \
  QFormLayout, QTableWidget, QTableWidgetItem


class Dialog(QWidget):
    def __init__(self, user, parent):
        super().__init__()
        self.url = 'http://localhost:5000/'

        self.parent = parent

        self.setFixedSize(300, 150)
        self.setWindowTitle(user["name"])
        self.user = user

        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QFormLayout()
        self.id = QLineEdit(self.user["id"])
        self.name = QLineEdit(self.user["name"])
        self.email = QLineEdit(self.user["email"])
        self.image = QLineEdit(self.user["bild"])
        layout.addRow(QLabel("Id"), self.id)
        layout.addRow(QLabel("Name"), self.name)
        layout.addRow(QLabel("Email"), self.email)
        layout.addRow(QLabel("Bild"), self.image)

        update = QPushButton("Update")
        update.clicked.connect(self.update)

        delete = QPushButton("Delete")
        delete.clicked.connect(self.delete)

        layout.addRow(update, delete)
        self.setLayout(layout)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:5000/schueler'

        self._width = 600
        self._height = 500
        self.list = None

        self.display_users()

        self.init_widgets()
        self.show()

    def display_users(self):
        self.users = requests.get(self.url).json()
        print(self.users)
        if self.list:
            self.list.clear()
            self.list.setRowCount(len(self.users))
            self.list.setHorizontalHeaderLabels(["Name", "Email", "Bild"])
        else:
            self.list = QTableWidget(self)
            self.list.setRowCount(len(self.users))
            self.list.setColumnCount(3)
            self.list.setHorizontalHeaderLabels(["Name", "Email", "Bild"])
            self.list.setFixedSize(self._width, 420)
            self.list.move(0, 80)

        row = 0

        for x in self.users['schueler']:
            self.list.setItem(row, 0, QTableWidgetItem(x["name"]))
            self.list.setItem(row, 1, QTableWidgetItem(x["email"]))
            self.list.setItem(row, 2, QTableWidgetItem(x["bild"]))
            row = row + 1


    def init_widgets(self):
        self.setFont(QFont("Sans Serif", 10))

        self.id_label = QLabel("id", self)
        self.id_label.move(5, 10)
        self.id_label = QLineEdit(self)
        self.id_label.resize(90, 29)
        self.id_label.move(5, 40)

        self.name_label = QLabel("Name", self)
        self.name_label.move(105, 10)
        self.name_input = QLineEdit(self)
        self.name_input.resize(90, 29)
        self.name_input.move(105, 40)

        self.email_label = QLabel("Email", self)
        self.email_label.move(205, 10)
        self.email_input = QLineEdit(self)
        self.email_input.resize(90, 29)
        self.email_input.move(205, 40)

        self.bild = QLabel("Bild", self)
        self.bild.move(305, 10)
        self.bild = QLineEdit(self)
        self.bild.resize(90, 29)
        self.bild.move(305, 40)

        self.msg = QLabel("", self)
        self.msg.setWordWrap(True)
        self.msg.setStyleSheet("* {color: red;}")
        self.msg.resize(290, 30)
        self.msg.move(405, 5)

        add = QPushButton("Insert", self)
        add.resize(90, 29)
        add.move(405, 40)

        cancel = QPushButton("Cancel", self)
        cancel.resize(90, 29)
        cancel.move(505, 40)

        self.setFixedSize(self._width, self._height)
        self.setWindowTitle('CRUD Client')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Main()
    sys.exit(app.exec_())
