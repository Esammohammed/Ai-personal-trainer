# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from GUI import exercise_info
from GUI import exercise_yoga

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(380, 60, 1300, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)

        self.frame_4.setGeometry(QtCore.QRect(80, 60, 1161, 761))
        self.frame_4.setStyleSheet("background-color: #f8f8f8;")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=50, color=QColor("black")
        )
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

        self.frame_4.setGraphicsEffect(effect)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.resize(1140, 833)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(150, 420, 300, 101))
        self.pushButton.clicked.connect(lambda: self.workout_ex(self.frame_4))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#2b3942;\n"
"color:white;\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #1f292f;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 420, 300, 101))
        self.pushButton_2.clicked.connect(lambda: self.yoga_ex(self.frame_4))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:#2b3942;\n"
"color:white;\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #1f292f;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Workout"))
        self.pushButton_2.setText(_translate("MainWindow", "Yoga"))
        self.label_11.setText(_translate("MainWindow", "Exercise Type"))
        self.label_11.setStyleSheet("color : white")

    def workout_ex(self ,frame):

        self.exinfoFrame = QtWidgets.QFrame(self.centralwidget)
        self.exinfoFrame.setGeometry(QtCore.QRect(80, 60, 0, 0))

        self.exinfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exinfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exinfoFrame.setObjectName("exinfoFrame")

        ui = exercise_info.Ui_Frame()
        ui.setupUi(self.exinfoFrame)
        self.exinfoFrame.show()
        frame.hide()
    def yoga_ex(self ,frame):

        self.exyogaFrame = QtWidgets.QFrame(self.centralwidget)
        self.exyogaFrame.setGeometry(QtCore.QRect(80, 60, 0, 0))

        self.exyogaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exyogaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exyogaFrame.setObjectName("exyogaFrame")

        ui = exercise_yoga.Ui_Frame()
        ui.setupUi(self.exyogaFrame)
        self.exyogaFrame.show()
        frame.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
