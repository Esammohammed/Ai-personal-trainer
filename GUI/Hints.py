
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QLineEdit, QWidget, QPlainTextEdit, QTextEdit


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

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())



