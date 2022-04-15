from PyQt5 import QtCore, QtGui, QtWidgets
from Database import DBoperation
up = DBoperation.database_operations
#data = ('102', '2', '3', '4', None, None, None, None, None)
class Ui_MainWindow1(object):
    def __init__(self, u):
        global data
        data = u
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1000)
        MainWindow.setStyleSheet("background-color: rgb(0, 45, 67);")
        MainWindow.setGeometry(QtCore.QRect(380, 60, 1300, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(80, 60, 1161, 761))
        self.frame_3.setStyleSheet("background-color: #f8f8f8;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(60, 140, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(610, 220, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget_13 = QtWidgets.QWidget(self.frame_3)
        self.widget_13.setGeometry(QtCore.QRect(60, 190, 501, 501))
        self.widget_13.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget#widget_17,#widget_18,#widget_19,#widget_20,#widget_21{\n"
"  border: 1px solid #d4d4d4;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.widget_13.setObjectName("widget_13")
        self.widget_17 = QtWidgets.QWidget(self.widget_13)
        self.widget_17.setGeometry(QtCore.QRect(0, 0, 501, 101))
        self.widget_17.setStyleSheet("")
        self.widget_17.setObjectName("widget_17")
        self.label_5 = QtWidgets.QLabel(self.widget_17)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QTextEdit(self.widget_17)
        self.name.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.b1 = QtWidgets.QPushButton(self.widget_17 ,clicked=lambda: self.name.setReadOnly(False) )
        self.b1.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b1.setStyleSheet("")
        self.b1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b1.setIcon(icon)
        self.b1.setIconSize(QtCore.QSize(22, 22))
        self.b1.setAutoDefault(False)
        self.b1.setDefault(False)
        self.b1.setObjectName("b1")
        self.widget_18 = QtWidgets.QWidget(self.widget_13)
        self.widget_18.setGeometry(QtCore.QRect(0, 100, 501, 101))
        self.widget_18.setStyleSheet("")
        self.widget_18.setObjectName("widget_18")
        self.label_28 = QtWidgets.QLabel(self.widget_18)
        self.label_28.setGeometry(QtCore.QRect(10, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.b2 = QtWidgets.QPushButton(self.widget_18,clicked=lambda: self.user.setReadOnly(False))
        self.b2.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b2.setStyleSheet("")
        self.b2.setText("")
        self.b2.setIcon(icon)
        self.b2.setIconSize(QtCore.QSize(22, 22))
        self.b2.setAutoDefault(False)
        self.b2.setDefault(False)
        self.b2.setObjectName("b2")
        self.user = QtWidgets.QTextEdit(self.widget_18)
        self.user.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user.setFont(font)
        self.user.setReadOnly(True)
        self.user.setObjectName("user")
        self.widget_19 = QtWidgets.QWidget(self.widget_13)
        self.widget_19.setGeometry(QtCore.QRect(0, 200, 501, 101))
        self.widget_19.setStyleSheet("")
        self.widget_19.setObjectName("widget_19")
        self.label_30 = QtWidgets.QLabel(self.widget_19)
        self.label_30.setGeometry(QtCore.QRect(10, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.email = QtWidgets.QTextEdit(self.widget_19)
        self.email.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setReadOnly(True)
        self.email.setObjectName("email")
        self.b3 = QtWidgets.QPushButton(self.widget_19,clicked=lambda: self.email.setReadOnly(False))
        self.b3.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b3.setStyleSheet("")
        self.b3.setText("")
        self.b3.setIcon(icon)
        self.b3.setIconSize(QtCore.QSize(22, 22))
        self.b3.setAutoDefault(False)
        self.b3.setDefault(False)
        self.b3.setObjectName("b3")
        self.widget_20 = QtWidgets.QWidget(self.widget_13)
        self.widget_20.setGeometry(QtCore.QRect(0, 300, 501, 101))
        self.widget_20.setStyleSheet("")
        self.widget_20.setObjectName("widget_20")
        self.label_32 = QtWidgets.QLabel(self.widget_20)
        self.label_32.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.password = QtWidgets.QTextEdit(self.widget_20)
        self.password.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setReadOnly(True)
        self.password.setObjectName("password")
        self.b4 = QtWidgets.QPushButton(self.widget_20,clicked=lambda: self.password.setReadOnly(False))
        self.b4.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b4.setStyleSheet("")
        self.b4.setText("")
        self.b4.setIcon(icon)
        self.b4.setIconSize(QtCore.QSize(22, 22))
        self.b4.setAutoDefault(False)
        self.b4.setDefault(False)
        self.b4.setObjectName("b4")
        self.widget_21 = QtWidgets.QWidget(self.widget_13)
        self.widget_21.setGeometry(QtCore.QRect(0, 400, 501, 101))
        self.widget_21.setStyleSheet("")
        self.widget_21.setObjectName("widget_21")
        self.label_36 = QtWidgets.QLabel(self.widget_21)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.b5 = QtWidgets.QPushButton(self.widget_21,clicked=lambda: self.age.setReadOnly(False))
        self.b5.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b5.setStyleSheet("")
        self.b5.setText("")
        self.b5.setIcon(icon)
        self.b5.setIconSize(QtCore.QSize(22, 22))
        self.b5.setAutoDefault(False)
        self.b5.setDefault(False)
        self.b5.setObjectName("b5")
        self.age = QtWidgets.QTextEdit(self.widget_21)
        self.age.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.age.setFont(font)
        self.age.setReadOnly(True)
        self.age.setObjectName("age")
        self.widget_14 = QtWidgets.QWidget(self.frame_3)
        self.widget_14.setGeometry(QtCore.QRect(610, 270, 501, 401))
        self.widget_14.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget#widget_27,#widget_28,#widget_29,#widget_30{\n"
"  border:1px solid #d4d4d4;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.widget_14.setObjectName("widget_14")
        self.widget_27 = QtWidgets.QWidget(self.widget_14)
        self.widget_27.setGeometry(QtCore.QRect(0, 0, 501, 101))
        self.widget_27.setStyleSheet("#widget_17{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_27.setObjectName("widget_27")
        self.label_10 = QtWidgets.QLabel(self.widget_27)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.b6 = QtWidgets.QPushButton(self.widget_27 ,clicked=lambda: self.height.setReadOnly(False))
        self.b6.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b6.setStyleSheet("")
        self.b6.setText("")
        self.b6.setIcon(icon)
        self.b6.setIconSize(QtCore.QSize(22, 22))
        self.b6.setAutoDefault(False)
        self.b6.setDefault(False)
        self.b6.setObjectName("b6")
        self.height = QtWidgets.QTextEdit(self.widget_27)
        self.height.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.height.setFont(font)
        self.height.setReadOnly(True)
        self.height.setObjectName("height")
        self.widget_28 = QtWidgets.QWidget(self.widget_14)
        self.widget_28.setGeometry(QtCore.QRect(0, 100, 501, 101))
        self.widget_28.setStyleSheet("#widget_18{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_28.setObjectName("widget_28")
        self.label_44 = QtWidgets.QLabel(self.widget_28)
        self.label_44.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.b7 = QtWidgets.QPushButton(self.widget_28,clicked=lambda: self.weight.setReadOnly(False))
        self.b7.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b7.setStyleSheet("")
        self.b7.setText("")
        self.b7.setIcon(icon)
        self.b7.setIconSize(QtCore.QSize(22, 22))
        self.b7.setAutoDefault(False)
        self.b7.setDefault(False)
        self.b7.setObjectName("b7")
        self.weight = QtWidgets.QTextEdit(self.widget_28)
        self.weight.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight.setFont(font)
        self.weight.setReadOnly(True)
        self.weight.setObjectName("weight")
        self.widget_29 = QtWidgets.QWidget(self.widget_14)
        self.widget_29.setGeometry(QtCore.QRect(0, 200, 501, 101))
        self.widget_29.setStyleSheet("#widget_19{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_29.setObjectName("widget_29")
        self.label_46 = QtWidgets.QLabel(self.widget_29)
        self.label_46.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gender = QtWidgets.QTextEdit(self.widget_29)
        self.gender.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gender.setFont(font)
        self.gender.setReadOnly(True)
        self.gender.setObjectName("gender")
        self.b8 = QtWidgets.QPushButton(self.widget_29,clicked=lambda: self.gender.setReadOnly(False))
        self.b8.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b8.setStyleSheet("")
        self.b8.setText("")
        self.b8.setIcon(icon)
        self.b8.setIconSize(QtCore.QSize(22, 22))
        self.b8.setAutoDefault(False)
        self.b8.setDefault(False)
        self.b8.setObjectName("b8")
        self.widget_30 = QtWidgets.QWidget(self.widget_14)
        self.widget_30.setGeometry(QtCore.QRect(0, 300, 501, 101))
        self.widget_30.setStyleSheet("#widget_20{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_30.setObjectName("widget_30")
        self.label_48 = QtWidgets.QLabel(self.widget_30)
        self.label_48.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.b9 = QtWidgets.QPushButton(self.widget_30,clicked=lambda: self.level.setReadOnly(False))
        self.b9.setGeometry(QtCore.QRect(460, 40, 31, 31))
        self.b9.setStyleSheet("")
        self.b9.setText("")
        self.b9.setIcon(icon)
        self.b9.setIconSize(QtCore.QSize(22, 22))
        self.b9.setAutoDefault(False)
        self.b9.setDefault(False)
        self.b9.setObjectName("b9")
        self.level = QtWidgets.QTextEdit(self.widget_30)
        self.level.setGeometry(QtCore.QRect(240, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.level.setFont(font)
        self.level.setReadOnly(True)
        self.level.setObjectName("level")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(569, 190, 31, 501))
        self.line.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(520, 0, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(540, 50, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.frame_3 )
        self.pushButton.clicked.connect(lambda:self.calldatabase())
        self.pushButton.setGeometry(QtCore.QRect(510, 720, 191, 51))
        font = QtGui.QFont()

        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 45, 67);\n"
"border-radius:20px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover{\n"
"background-color: rgb(10, 60, 75);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Basic information"))
        self.label_3.setText(_translate("MainWindow", "Extra infotmation"))
        self.label_5.setText(_translate("MainWindow", "Full name"))
        self.label_28.setText(_translate("MainWindow", "Username"))
        self.label_30.setText(_translate("MainWindow", "Email"))
        self.label_32.setText(_translate("MainWindow", "Password"))
        self.label_36.setText(_translate("MainWindow", "Age"))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.label_44.setText(_translate("MainWindow", "Weight"))
        self.label_46.setText(_translate("MainWindow", "Gender"))
        self.label_48.setText(_translate("MainWindow", "Level"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.user.setText(_translate("MainWindow", data[0]))
        self.name.setText(_translate("MainWindow", data[1]))
        self.email.setText(_translate("MainWindow", data[2]))
        self.password.setText(_translate("MainWindow", data[3]))
        self.age.setText(_translate("MainWindow", data[4]))
        self.height.setText(_translate("MainWindow", str(data[5])))
        self.weight.setText(_translate("MainWindow", str(data[6])))
        self.level.setText(_translate("MainWindow", data[7]))
        self.gender.setText(_translate("MainWindow", data[8]))
        self.label_11.setText(_translate("MainWindow", data[0]))
        self.label_12.setText(_translate("MainWindow", data[1]))
    def calldatabase(self):
        up.Update(self.user.toPlainText()
               , self.name.toPlainText(), self.email.toPlainText(),
               self.password.toPlainText(), int(self.age.toPlainText()), self.height.toPlainText(), self.weight.toPlainText(),
                  self.level.toPlainText(),
               self.gender.toPlainText())
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QFrame()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())