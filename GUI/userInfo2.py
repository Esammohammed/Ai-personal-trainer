from PyQt5 import QtCore, QtGui, QtWidgets
from Database import DBoperation
class Ui_MainWindow(object):

    def __init__(self,u):
        global data
        data=u
        print("lol")

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 20, 1131, 821))
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
"QPushButton{\n"
"    \n"
"  border: none;\n"
"\n"
"}\n"
"")
        self.widget_13.setObjectName("widget_13")
        self.widget_17 = QtWidgets.QWidget(self.widget_13)
        self.widget_17.setGeometry(QtCore.QRect(0, 0, 501, 101))
        self.widget_17.setStyleSheet("")
        self.widget_17.setObjectName("widget_17")
        self.label_6 = QtWidgets.QLabel(self.widget_17)
        self.label_6.setGeometry(QtCore.QRect(259, 10, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.widget_17)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_17 , )
        self.pushButton_7.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.widget_18 = QtWidgets.QWidget(self.widget_13)
        self.widget_18.setGeometry(QtCore.QRect(0, 100, 501, 101))
        self.widget_18.setStyleSheet("")
        self.widget_18.setObjectName("widget_18")
        self.label_27 = QtWidgets.QLabel(self.widget_18)
        self.label_27.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.widget_18)
        self.label_28.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_19 = QtWidgets.QWidget(self.widget_13)
        self.widget_19.setGeometry(QtCore.QRect(0, 200, 501, 101))
        self.widget_19.setStyleSheet("")
        self.widget_19.setObjectName("widget_19")
        self.label_29 = QtWidgets.QLabel(self.widget_19)
        self.label_29.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget_19)
        self.label_30.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_20 = QtWidgets.QWidget(self.widget_13)
        self.widget_20.setGeometry(QtCore.QRect(0, 300, 501, 101))
        self.widget_20.setStyleSheet("")
        self.widget_20.setObjectName("widget_20")
        self.label_31 = QtWidgets.QLabel(self.widget_20)
        self.label_31.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.widget_20)
        self.label_32.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_20)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_21 = QtWidgets.QWidget(self.widget_13)
        self.widget_21.setGeometry(QtCore.QRect(0, 400, 501, 101))
        self.widget_21.setStyleSheet("")
        self.widget_21.setObjectName("widget_21")
        self.label_35 = QtWidgets.QLabel(self.widget_21)
        self.label_35.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.widget_21)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_14 = QtWidgets.QWidget(self.frame_3)
        self.widget_14.setGeometry(QtCore.QRect(610, 270, 501, 401))
        self.widget_14.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget#widget_27,#widget_28,#widget_29,#widget_30{\n"
"  border:1px solid #d4d4d4;\n"
"}\n"
"QPushButton{\n"
"border : none;\n"
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
        self.label_9 = QtWidgets.QLabel(self.widget_27)
        self.label_9.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_27)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_27)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QtCore.QSize(37, 22))
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.widget_28 = QtWidgets.QWidget(self.widget_14)
        self.widget_28.setGeometry(QtCore.QRect(0, 100, 501, 101))
        self.widget_28.setStyleSheet("#widget_18{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_28.setObjectName("widget_28")
        self.label_43 = QtWidgets.QLabel(self.widget_28)
        self.label_43.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.widget_28)
        self.label_44.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_28)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(37, 22))
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.widget_29 = QtWidgets.QWidget(self.widget_14)
        self.widget_29.setGeometry(QtCore.QRect(0, 200, 501, 101))
        self.widget_29.setStyleSheet("#widget_19{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_29.setObjectName("widget_29")
        self.label_45 = QtWidgets.QLabel(self.widget_29)
        self.label_45.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.widget_29)
        self.label_46.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_29)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QtCore.QSize(37, 22))
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.widget_30 = QtWidgets.QWidget(self.widget_14)
        self.widget_30.setGeometry(QtCore.QRect(0, 300, 501, 101))
        self.widget_30.setStyleSheet("#widget_20{\n"
"    \n"
"  border: 1px solid black;\n"
"\n"
"}")
        self.widget_30.setObjectName("widget_30")
        self.label_47 = QtWidgets.QLabel(self.widget_30)
        self.label_47.setGeometry(QtCore.QRect(259, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.widget_30)
        self.label_48.setGeometry(QtCore.QRect(10, 10, 240, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_30)
        self.pushButton_14.setGeometry(QtCore.QRect(460, 30, 31, 31))
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QtCore.QSize(37, 22))
        self.pushButton_14.setAutoDefault(False)
        self.pushButton_14.setDefault(False)
        self.pushButton_14.setObjectName("pushButton_14")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
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
        self.label.setText(_translate("MainWindow", "Basic information"))
        self.label_3.setText(_translate("MainWindow", "Extra infotmation"))
        self.label_6.setText(_translate("MainWindow", data[0]))
        self.label_5.setText(_translate("MainWindow", "Full name"))
        self.label_27.setText(_translate("MainWindow", data[1]))
        self.label_28.setText(_translate("MainWindow", "Username"))
        self.label_29.setText(_translate("MainWindow",data[2]))
        self.label_30.setText(_translate("MainWindow", "Email"))
        self.label_31.setText(_translate("MainWindow", data[3]))
        self.label_32.setText(_translate("MainWindow", "Password"))
        self.label_35.setText(_translate("MainWindow", data[4]))
        self.label_36.setText(_translate("MainWindow", "Age"))
        self.label_9.setText(_translate("MainWindow", data[5]))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.label_43.setText(_translate("MainWindow", data[6]))
        self.label_44.setText(_translate("MainWindow", "Weight"))
        self.label_45.setText(_translate("MainWindow", data[7]))
        self.label_46.setText(_translate("MainWindow", "Gender"))
        self.label_47.setText(_translate("MainWindow", data[8]))
        self.label_48.setText(_translate("MainWindow", "Level"))
        self.label_11.setText(_translate("MainWindow", data[0]))
        self.label_12.setText(_translate("MainWindow", data[1]))

        self.user.setText(_translate("MainWindow", data[0]))

        self.name.setText(_translate("MainWindow", data[1]))

        self.email.setText(_translate("MainWindow", data[2]))

        self.password.setText(_translate("MainWindow", data[3]))

        self.age.setText(_translate("MainWindow", data[4]))

        self.height.setText(_translate("MainWindow", data[5]))

        self.weight.setText(_translate("MainWindow", data[6]))

        self.level.setText(_translate("MainWindow", data[7]))

        self.gender.setText(_translate("MainWindow", data[8]))

        self.name.setText(_translate("MainWindow", data[0]))
        self.user.setText(_translate("MainWindow", data[1]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
