
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from Database import DBoperation



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(2000, 1000)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame = QtWidgets.QFrame(Dialog)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 2000, 841))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.frame_2 = QtWidgets.QFrame(self.MainFrame)
        self.frame_2.setGeometry(QtCore.QRect(80, 70, 1300, 761))
        self.frame_2.setStyleSheet("background-color:#7996C3;\n"
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
"background-color:#03416E;\n"
"color:white;\n"
"border-radius: 10px;\n"
"box-shadow: 5px 10px #888888;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: #042940;\n"
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
"background-color:#03416E;\n"
"color:white;\n"
"border-radius: 10px;\n"
"box-shadow: 5px 10px #888888;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: #042940;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(190, 290, 761, 161))
        self.frame.setStyleSheet("background-color:#042940;\n"
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
        self.label_13.setGeometry(QtCore.QRect(580, 70, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1300, 261))
        self.frame_3.setStyleSheet("background-color: #03416E;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(470, 120, 371, 81))
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
        self.label_12.setText(_translate("Dialog", "Date"))
        self.label_13.setText(_translate("Dialog", "20/3/2022"))
        self.label.setText(_translate("Dialog", "Achievements"))

    def getPrevious(self):
        result = DBoperation.database_operations.GetAchievements('1')
        print(str(result[0]))
        self.label_4.setText(str(result[0][0]))
        self.label_11.setText(str(result[0][2]))
        self.label_13.setText(str(result[0][3]))

    def getnext(self):
        self.label_4.setText("Next")
        self.label_11.setText("2000")
        self.label_13.setText("20/3/2000")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
