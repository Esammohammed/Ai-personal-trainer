# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Achievements.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from Database import DBoperation



class Ui_Dialog(object):
    def __init__(self, u):
        global data
        global result
        global counter
        self.counter = 0
        data = u
        result = DBoperation.database_operations.GetAchievements(data[0])
        print(result)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(2000, 1000)
        Dialog.setGeometry(QtCore.QRect(380, 60, 1300, 900))
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)


        self.frame_2.setGeometry(QtCore.QRect(80, 60, 1161, 761))
        self.frame_2.resize(1140, 833)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=50, color=QColor("black")
        )
        self.frame_2.setGraphicsEffect(effect)

        self.frame_2.setStyleSheet("background-color: #f8f8f8;\n"
"\n"
"QPushButton{\n"
" background-color: #333333;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 520, 201, 51))
        self.pushButton_2.clicked.connect(lambda : self.getPrevious())


        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("*{\n"
"background-color:#2b3942;\n"
"color:white;\n"
"border-radius: 10px;\n"
"box-shadow: 5px 10px #888888;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: #2b3942;\n"
"    transition-duration: 2s;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(740, 520, 201, 51))
        self.pushButton.clicked.connect(lambda : self.getnext())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("*{\n"
"background-color:#2b3942;\n"
"color:white;\n"
"border-radius: 10px;\n"
"box-shadow: 5px 10px #888888;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: #2b3942;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(190, 290, 761, 161))
        self.frame.setStyleSheet("background-color:#2b3942;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 70, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(360, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(380, 70, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(600, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(600, 70, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)

        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1161, 111))
        self.frame_3.setStyleSheet("background-color:#2b3942;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)

        self.label.setGeometry(QtCore.QRect(450, 40, 254, 46))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Previous Exercise"))
        self.pushButton.setText(_translate("Dialog", "Next Exercise"))
        self.label_2.setText(_translate("Dialog", "Exercise Name"))
        self.label_4.setText(_translate("Dialog", "Name"))
        self.label_10.setText(_translate("Dialog", "Best Score"))
        self.label_11.setText(_translate("Dialog", "Score"))
        self.label_12.setText(_translate("Dialog", "Type"))
        if len(result) == 0:
            self.label_4.setText(_translate("Dialog", "-"))
            self.label_11.setText(_translate("Dialog", "-"))
            self.label_13.setText(_translate("Dialog", "-"))
            self.pushButton_2.hide()
            self.pushButton.hide()
        else:
            self.label_4.setText(_translate("Dialog", str(result[0][0])))
            self.label_11.setText(_translate("Dialog", str(result[0][2])))
            self.label_13.setText(_translate("Dialog", str(result[0][3])))

        self.label.setText(_translate("Dialog", "Achievements"))

    def getPrevious(self):
        if self.counter < 0:
            self.counter = len(result) - 1
        self.label_4.setText(str(result[self.counter][0]))
        self.label_11.setText(str(result[self.counter][2]))
        self.label_13.setText(str(result[self.counter][3]))
        self.counter = self.counter - 1

    def getnext(self):
        if self.counter == len(result):
            self.counter = 0
        self.label_4.setText(str(result[self.counter][0]))
        self.label_11.setText(str(result[self.counter][2]))
        self.label_13.setText(str(result[self.counter][3]))
        self.counter = self.counter + 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
