from sys import argv,exit
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit, QMessageBox, QLineEdit, QLabel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
import threading
import time as tme
import tkinter
from tkinter import filedialog
import serial

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.status = True
        self.status2 = True
        self.initUI()

    def initUI(self):  # creating widgets
        self.qbtn = QPushButton('Start', self)  # button Start/Stop
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 50)
        self.qbtn.setGeometry(QtCore.QRect(325, 170, 180, 34))
        self.qbtn.setStyleSheet("QPushButton { background-color: rgb(0, 255,0) }"
                                "QPushButton:pressed { background-color: red }")
        self.setGeometry(100, 100, 600, 575)
        self.setWindowTitle('Quit button')
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(75, 70, 180, 30))
        self.lineEdit_1.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_1.setObjectName("PORT")
        font = self.lineEdit_1.font()
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setText("COM5")
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(325, 70, 180, 30))
        self.lineEdit_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("CONNECTION_SPEED")
        font = self.lineEdit_2.font()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setText("9600")
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(75, 170, 180, 30))
        self.lineEdit_3.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("TIMEOUT")
        font = self.lineEdit_3.font()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setText("1")
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(150, 40, 70, 30))
        self.label_1.setObjectName("label_1")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Port:")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(355, 40, 150, 30))
        self.label_2.setObjectName("label_1")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_1")
        self.label_2.setText("Connection speed:")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(136, 140, 70, 30))
        self.label_3.setObjectName("label_1")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_1")
        self.label_3.setText("Timeout:")
        self.Text = QTextEdit(self)
        self.Text.setGeometry(75, 250, 430, 275)
        self.Text.moveCursor(QtGui.QTextCursor.End)
        self.Text.ensureCursorVisible()
        self.qbtn.clicked.connect(self.path_file)
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(120, 533, 400, 30))
        self.label_4.setObjectName("label_1")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("©СПХФУ Лаборатория аддитивных технологий")
        self.path = ""

    def path_file(self):
        if self.status2 == True:
            root = tkinter.Tk()
            root.withdraw()
            self.path = filedialog.asksaveasfilename(confirmoverwrite=False)
        self.threading_conductor()
    def threading_conductor(self):
        try:
            t = threading.Thread(target=self.conductor)
            t.daemon = True
            t.start()


        except Exception as err:
            print("threading_conductor: ", err)

    def threading_console(self):
        t = threading.Thread(target=self.console)
        t.daemon = True
        t.start()

    def console(self):
        try:
            read = open(self.path, "r")
            while self.status == True:

                file = read.readline()
                if not file =="":
                    self.Text.append(file)

        except Exception as err:
            print("console: wrong path: ", err)

    def conductor(self):    # parent readport
        if self.qbtn.text() == "Start":
            self.status = True
            self.status2 = False
            self.qbtn.setText("Stop")
            self.qbtn.setStyleSheet("QPushButton { background-color: red }"
                                    "QPushButton:pressed { background-color: red }")
            port, connection_speed, timeout = self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text()
            if not "." in self.path:
                self.path = self.path + ".csv"

                log_file = open(self.path, 'a')
                log_file.close()
            else:
                log_file = open(self.path, 'a')
                log_file.close()
            self.threading_console()
            try:
                ser = serial.Serial(port=port, baudrate=connection_speed, timeout=int(timeout))
                while self.status == True:
                    serialString = ser.readline()
                    data_str = serialString.decode('UTF-8').replace("\n","")
                    now = str(round(tme.time(), 2))

                    if data_str != "":
                        log_file = open(self.path, 'a')
                        log_file.write(str(now) + ',' + str(data_str))
                        log_file.close()
                    tme.sleep(0.1)

            except:
                self.qbtn.setText("Start")
                self.qbtn.setStyleSheet("QPushButton { background-color: rgb(0, 255,0) }"
                                        "QPushButton:pressed { background-color: rgb(0, 255,0) }")
                QMessageBox.critical(self, "Ошибка подключения ", "Неправильные введенные данные или занят порт", QMessageBox.Ok)
                self.status = True

        elif self.qbtn.text() == "Stop":
            self.status2 = True
            self.status = False
            self.qbtn.setText("Start")
            self.qbtn.setStyleSheet("QPushButton { background-color: rgb(0, 255,0) }"
                              "QPushButton:pressed { background-color: rgb(0, 255,0) }")



if __name__ == '__main__':
    app = QApplication(argv)
    ex = Example()
    ex.setWindowTitle("Port Monitoring")
    ex.show()
    exit(app.exec_())