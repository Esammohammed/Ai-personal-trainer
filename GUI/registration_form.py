# -*- coding: utf
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Login_page
from PyQt5.QtWidgets import QMessageBox


from Database import DBoperation
import hashlib
import os

DBoperations = DBoperation.database_operations
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 834)
        MainWindow.setStyleSheet("background-color:#2b3942")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 50, 581, 711))
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
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 460, 491, 60))
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
        self.Login = QtWidgets.QPushButton(self.widget , clicked=lambda: self.register_Db())
        self.Login.setGeometry(QtCore.QRect(20, 560, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.widget , clicked= lambda : self.open_login(MainWindow))

        self.pushButton_2.setGeometry(QtCore.QRect(160, 640, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:rgb(99, 99, 99);\n"
"border:1px;}\n"
"QPushButton:hover{\n"
"color:rgb(135, 135, 135);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 220, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"\n"
"borde-bottom:5px solid;\n"
"border-bottom-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 57, 255, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"padding-left:10px\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 300, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"\n"
"borde-bottom:5px solid;\n"
"border-bottom-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 57, 255, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"padding-left:10px\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 380, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color:rgb(0, 0, 0);\n"
"\n"
"borde-bottom:5px solid;\n"
"border-bottom-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 57, 255, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"padding-left:10px\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def register_Db(self):
        print ("dasd")
        if self.lineEdit.text()== "" or self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "" or self.lineEdit_5.text() == "" \
                or self.lineEdit_2.text()== "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields Are Required")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            try:

                con = pymysql.connect(host="localhost", user="root", password="1234",)
                cur = con.cursor()
                cur.execute("select * from e_trainer.userr where idUser=%s"
                            , self.lineEdit_4.text())
                row = cur.fetchone()

                if row != None:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("User already Exist,Please try with another User")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:


                    DBoperations.insert(self.lineEdit_4.text() ,self.lineEdit.text(), self.lineEdit_5.text(),

                                   self.lineEdit_2.text(), int(self.lineEdit_3.text()), None,None,None,None)

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Register Succesfull")
                    msg.setWindowTitle("success")
                    msg.exec_()

            except Exception as es:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("errorrrrrrr")
                msg.setWindowTitle("success")
                msg.exec_()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the  Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the Password"))
        self.Login.setText(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton_2.setText(_translate("MainWindow", "Already registered?"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter the Age"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter the Username"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter the E-mail"))

    def open_login(self,MainWindow):

        self.window = QtWidgets.QMainWindow()
        self.ui = Login_page.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
