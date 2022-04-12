# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QApplication



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        layoutGrid = QGridLayout();

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 616)
        MainWindow.setStyleSheet("*{\n"
"background-color:#FFFFFF;\n"
"padding:0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.exercises = QtWidgets.QPushButton(self.centralwidget)
        self.exercises.setGeometry(QtCore.QRect(0, 110, 300, 51))
        self.exercises.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#302a75;\n"
"color:#FFFFFF;\n"
"}")
        self.exercises.setObjectName("exercises")
        self.exercises.clicked.connect(self.showEx)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 300, 1050))
        self.listView.setMinimumSize(QtCore.QSize(0, 621))
        self.listView.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"height:100px;\n"
"\n"
"}")
        self.listView.setObjectName("listView")

        self.userInfo = QtWidgets.QPushButton(self.centralwidget)
        self.userInfo.setGeometry(QtCore.QRect(0, 170, 300, 51))
        self.userInfo.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#302a75;\n"
"color:#FFFFFF;\n"
"}")
        self.userInfo.setObjectName("userInfo")
        self.userInfo.clicked.connect(self.showUs)

        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(0, 220, 300, 51))
        self.history.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#302a75;\n"
"color:#FFFFFF;\n"
"}")
        self.history.setObjectName("history")
        self.history.clicked.connect(self.showHis)

        self.achievements = QtWidgets.QPushButton(self.centralwidget)
        self.achievements.setGeometry(QtCore.QRect(0, 270, 300, 51))
        self.achievements.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#302a75;\n"
"color:#FFFFFF;\n"
"}")
        self.achievements.setObjectName("achievements")
        self.achievements.clicked.connect(self.showAch)

        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(0, 330, 300, 51))
        self.EXIT.setStyleSheet("*{\n"
"background-color:#10454F;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#302a75;\n"
"color:#FFFFFF;\n"
"}")
        self.EXIT.setObjectName("EXIT")
        self.exFrame = QtWidgets.QFrame(self.centralwidget)
        self.exFrame.setGeometry(QtCore.QRect(210, -10, 591, 631))
        self.exFrame.setStyleSheet("background-color:white;\n"
"display:none;")
        self.exFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exFrame.setObjectName("exFrame")
        self.label = QtWidgets.QLabel(self.exFrame)
        self.label.setGeometry(QtCore.QRect(200, 30, 191, 61))
        self.label.setStyleSheet("font-weight:900;\n"
"background-color:gray;")
        self.label.setObjectName("label")
        self.usFrame = QtWidgets.QFrame(self.centralwidget)
        self.usFrame.setGeometry(QtCore.QRect(210, -10, 591, 631))
        self.usFrame.setStyleSheet("background-color:white;")
        self.usFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usFrame.setObjectName("exFrame")
        self.label5 = QtWidgets.QLabel(self.usFrame)
        self.label5.setGeometry(QtCore.QRect(200, 30, 191, 61))
        self.label5.setStyleSheet("font-weight:900;\n"
                                 "background-color:gray;")
        self.label5.setObjectName("label5")
        self.label5.setText('user info')
        self.hisframe = QtWidgets.QFrame(self.centralwidget)
        self.hisframe.setGeometry(QtCore.QRect(210, -10, 591, 631))
        self.hisframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hisframe.setStyleSheet("background-color:white;")
        self.hisframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hisframe.setObjectName("hisframe")
        self.label_4 = QtWidgets.QLabel(self.hisframe)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 91, 41))
        self.label_4.setStyleSheet("background-color:gray;")
        self.label_4.setObjectName("label_4")

        self.achFrame = QtWidgets.QFrame(self.centralwidget)
        self.achFrame.setGeometry(QtCore.QRect(210, -10, 591, 631))
        self.achFrame.setStyleSheet("background-color:white;")
        self.achFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.achFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.achFrame.setObjectName("achFrame")
        self.label_5 = QtWidgets.QLabel(self.achFrame)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 131, 41))
        self.label_5.setStyleSheet("background-color:gray;")
        self.label_5.setObjectName("label_5")
        self.EXIT.clicked.connect(sys.exit)
        self.exFrame.raise_()
        self.listView.raise_()
        self.exercises.raise_()
        self.userInfo.raise_()
        self.history.raise_()
        self.achievements.raise_()
        self.EXIT.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exercises.setText(_translate("MainWindow", "Exercises"))
        self.userInfo.setText(_translate("MainWindow", "Show User Info"))
        self.history.setText(_translate("MainWindow", "History"))
        self.achievements.setText(_translate("MainWindow", "Achievements"))
        self.EXIT.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Exercises</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">History</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Achievements</span></p></body></html>"))
        self.exFrame.hide()
        self.usFrame.hide()
        self.hisframe.hide()
        self.achFrame.hide()

    def showEx(self):
        self.exFrame.show()
        self.hisframe.hide()
        self.achFrame.hide()
        self.usFrame.hide()

    def showUs(self):
        self.usFrame.show()
        self.hisframe.hide()
        self.achFrame.hide()
        self.exFrame.hide()


    def showHis(self):
        self.hisframe.show()
        self.achFrame.hide()
        self.usFrame.hide()
        self.exFrame.hide()

    def showAch(self):
        self.achFrame.show()
        self.hisframe.hide()
        self.usFrame.hide()
        self.exFrame.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
