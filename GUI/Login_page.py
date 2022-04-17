import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import use

from GUI import registration_form
from PyQt5.QtWidgets import QMessageBox
from Database import DBoperation
import mainWindow
import sys

DBoperations = DBoperation.database_operations
class Ui_MainWindow(object):


    def open_register(self,MainWindow):

        self.window = QtWidgets.QMainWindow()
        self.ui  =  registration_form.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.destroy()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 638)
        MainWindow.setStyleSheet("background-color:#2b3942")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 70, 561, 491))
        self.widget.setStyleSheet("background-color:#f8f8f8")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color:rgb(0, 0, 0);\n"
                                    
"\n"
"borde-bottom:5px solid;\n"
"border-bottom-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 57, 255, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"padding-left:10px\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 230, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"border-color: rgb(0, 170, 255);\n"
"padding-left:10px\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Login = QtWidgets.QPushButton(self.widget,clicked= lambda : self.login_DB(MainWindow))
        self.Login.setGeometry(QtCore.QRect(20, 320, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setStyleSheet("QPushButton{\n"
                                      "background-color: #2b3942;\n"
                                      "border-radius:20px;\n"
                                      "color:rgb(255, 255, 255);}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #1f292f;\n"
                                      "}")
        self.Login.setObjectName("Login")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget , clicked= lambda : self.open_register(MainWindow))
        self.pushButton_2.setGeometry(QtCore.QRect(190, 420, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:rgb(99, 99, 99);\n"
"border:1px;}\n"
"QPushButton:hover{\n"
"color:rgb(179, 179, 179);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the Password"))
        self.Login.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "Log in"))
        self.pushButton_2.setText(_translate("MainWindow", "sign up"))
    def login_DB(self,MainWindow):


        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields Are Required")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:

           try:
                row =DBoperations.select_user(self.lineEdit.text(),self.lineEdit_2.text())

                if row == None:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Invalid Username And Password")
                    msg.setWindowTitle("Error")
                    msg.exec_()

                else:

                    self.window = QtWidgets.QMainWindow()
                    self.ui = mainWindow.Ui_MainWindow(row)
                    self.ui.setupUi(self.window)
                    self.window.show()
                    MainWindow.destroy()

           except Exception as es:
               msg = QMessageBox()
               msg.setIcon(QMessageBox.Information)
               msg.setText("")
               msg.setWindowTitle("")
               msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
