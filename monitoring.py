import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextBrowser
from PyQt5 import QtCore, QtWidgets,QtGui
import os
import subprocess


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.status = True
        self.initUI()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        pipe_glob.kill()
        a0.accept()

    def initUI(self):
        self.qbtn = QPushButton('Start', self)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 50)
        self.qbtn.setGeometry(QtCore.QRect(325, 170, 180, 34))
        self.qbtn.setStyleSheet("QPushButton { background-color: rgb(0, 255,0) }"
                                "QPushButton:pressed { background-color: red }")
        self.setGeometry(100, 100, 600, 575)
        self.setWindowTitle('Quit button')
        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(75, 70, 180, 30))
        self.lineEdit_1.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_1.setObjectName("CollectionVessel_X")
        font = self.lineEdit_1.font()
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setText("COM5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(325, 70, 180, 30))
        self.lineEdit_2.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("CollectionVessel_X")
        font = self.lineEdit_2.font()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setText("9600")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(75, 170, 180, 30))
        self.lineEdit_3.setStyleSheet("background: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("CollectionVessel_X")
        font = self.lineEdit_3.font()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setText("1")
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(150, 40, 70, 30))
        self.label_1.setObjectName("label_1")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Port:")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(355, 40, 150, 30))
        self.label_2.setObjectName("label_1")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_1")
        self.label_2.setText("Connection speed:")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(136, 140, 70, 30))
        self.label_3.setObjectName("label_1")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_1")
        self.label_3.setText("Timeout:")
        self.Text = QTextBrowser(self)
        self.Text.setGeometry(75, 250, 430, 275)
        self.qbtn.clicked.connect(self.conductor)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(136, 540, 400, 30))
        self.label_4.setObjectName("label_1")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(55)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("©СПбГХВУ Лаборатория аддитивных технологий")




    def conductor(self):
        global pipe_glob

        if self.qbtn.text() == "Start":
            self.qbtn.setText("Stop")
            self.qbtn.setStyleSheet("QPushButton { background-color: red }"
                                    "QPushButton:pressed { background-color: red }")
            port = self.lineEdit_1.text()
            connection_speed = self.lineEdit_2.text()
            timeout = self.lineEdit_3.text()
            plot = os.path.join(os.path.dirname(__file__), "./other.py")
            path = [sys.executable, plot]
            pipe = subprocess.Popen(path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            pipe.stdin.write((port+" ").encode("utf8"))
            pipe.stdin.write((connection_speed+" ").encode("utf8"))
            pipe.stdin.write((timeout+" ").encode("utf8"))
            pipe.stdin.write((self.qbtn.text()+" ").encode("utf8"))
            pipe.stdin.close()
            pipe_glob = pipe



        elif self.qbtn.text() == "Stop":
            pipe_glob.kill()
            self.qbtn.setText("Start")
            self.qbtn.setStyleSheet("QPushButton { background-color: rgb(0, 255,0) }"
                              "QPushButton:pressed { background-color: rgb(0, 255,0) }")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setWindowTitle("Lebedev")
    ex.show()
    sys.exit(app.exec_())