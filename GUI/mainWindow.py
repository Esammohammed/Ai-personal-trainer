# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.Achievements import Ui_Dialog
from GUI.userInfo import Ui_MainWindow
from GUI.HistoryPage import Ui_Form
from GUI.exercise_info import Ui_Frame

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1000)
        MainWindow.setStyleSheet("*{\n"
"background-color:#FFFFFF;\n"
"padding:0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.exercises = QtWidgets.QPushButton(self.centralwidget)
        self.exercises.setGeometry(QtCore.QRect(0, 110, 300, 51))
        self.exercises.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#042940;\n"
"color:#FFFFFF;\n"
"}")
        self.exercises.setObjectName("exercises")
        self.exercises.clicked.connect(self.showEx)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 300, 1050))
        self.listView.setMinimumSize(QtCore.QSize(0, 621))
        self.listView.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"height:100px;\n"
"\n"
"}")
        self.listView.setObjectName("listView")

        self.userInfo = QtWidgets.QPushButton(self.centralwidget)
        self.userInfo.setGeometry(QtCore.QRect(0, 170, 300, 51))
        self.userInfo.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#042940;\n"
"color:#FFFFFF;\n"
"}")
        self.userInfo.setObjectName("userInfo")
        self.userInfo.clicked.connect(self.showUs)

        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(0, 220, 300, 51))
        self.history.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#042940;\n"
"color:#FFFFFF;\n"
"}")
        self.history.setObjectName("history")
        self.history.clicked.connect(self.showHis)

        self.achievements = QtWidgets.QPushButton(self.centralwidget)
        self.achievements.setGeometry(QtCore.QRect(0, 270, 300, 51))
        self.achievements.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#042940;\n"
"color:#FFFFFF;\n"
"}")
        self.achievements.setObjectName("achievements")
        self.achievements.clicked.connect(self.showAch)

        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(0, 330, 300, 51))
        self.EXIT.setStyleSheet("*{\n"
"background-color:#03416E;\n"
"color:#FFFFFF;\n"
"border:0px;\n"
"font-size:20px;\n"
"}\n"
"\n"
"*:hover{\n"
"background-color:#042940;\n"
"color:#FFFFFF;\n"
"}")
        self.EXIT.setObjectName("EXIT")
        self.exFrame = QtWidgets.QFrame(self.centralwidget)
        self.exFrame.setGeometry(QtCore.QRect(300, -10, 591, 631))
        self.exFrame.setStyleSheet("background-color:white;\n"
"display:none;")
        self.exFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exFrame.setObjectName("exFrame")

        self.usFrame = QtWidgets.QFrame(self.centralwidget)
        self.usFrame.setGeometry(QtCore.QRect(300, -10, 591, 631))
        self.usFrame.setStyleSheet("background-color:white;")
        self.usFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usFrame.setObjectName("exFrame")


        self.hisframe = QtWidgets.QFrame(self.centralwidget)
        self.hisframe.setGeometry(QtCore.QRect(300, -10, 591, 631))
        self.hisframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hisframe.setStyleSheet("background-color:white;")
        self.hisframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hisframe.setObjectName("hisframe")

        self.achFrame = QtWidgets.QFrame(self.centralwidget)
        self.achFrame.setGeometry(QtCore.QRect(300, -10, 591, 631))
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
        self.exFrame.hide()
        self.usFrame.hide()
        self.hisframe.hide()
        self.achFrame.hide()

    def showEx(self):
        ui = Ui_Frame()
        ui.setupUi(self.exFrame)
        self.exFrame.show()
        self.hisframe.hide()
        self.achFrame.hide()
        self.usFrame.hide()

    def showUs(self):
        ui = Ui_MainWindow()
        ui.setupUi(self.usFrame)
        self.usFrame.show()
        self.hisframe.hide()
        self.achFrame.hide()
        self.exFrame.hide()


    def showHis(self):
        ui = Ui_Form()
        ui.setupUi(self.hisframe)
        self.hisframe.show()
        self.achFrame.hide()
        self.usFrame.hide()
        self.exFrame.hide()

    def showAch(self):
        ui = Ui_Dialog()
        ui.setupUi(self.achFrame)
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

#   def getPrevious(self):
  #      self.label_4.setText("Previous")
   #     self.label_11.setText("1000")
    #    self.label_13.setText("20/3/2019")


   # def getnext(self):
    #    self.label_4.setText("Next")
     #   self.label_11.setText("2000")
      #  self.label_13.setText("20/3/2000")

      #self.pushButton_2.clicked.connect(self.getPrevious)
      #self.pushButton.clicked.connect(self.getnext)
