
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QLineEdit, QWidget, QPlainTextEdit, QTextEdit

import bicepscurl

import yoga_Side_angel
from GUI import exercise_info
from GUI import exercise_yoga
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QGraphicsDropShadowEffect
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(0, 0, 1161, 761))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.resize(1140, 833)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)

        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1161, 111))
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=50, color=QColor("black")
        )

        self.frame_4.setGraphicsEffect(effect)
        self.frame_4.setStyleSheet("background-color: #f8f8f8;")
        self.frame_4.setGraphicsEffect(effect)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.resize(1140, 833)
        self.header = QtWidgets.QFrame(self.frame_4)
        self.header.setGeometry(QtCore.QRect(0, 0, 1161, 111))
        self.header.setStyleSheet("background-color:#2b3942;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.label_11 = QtWidgets.QLabel(self.header)
        self.label_11.setGeometry(QtCore.QRect(450, 40, 254, 46))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(490, 480, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textbox =  QPlainTextEdit(self.frame_4)
        self.textbox.setGeometry(QtCore.QRect(20, 550, 1101, 201))
        self.textbox.setFont(QFont("Arial", 20))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hints"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())



