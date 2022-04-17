from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QGraphicsDropShadowEffect


#data = ('5', '2', '3', '4', None, None, None, None, None)


class Ui_Form(object):
    def __init__(self, u):
        global data
        data = u
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000, 1000)
        Form.setStyleSheet("background-color: rgb(0, 45, 67);")
        Form.setGeometry(QtCore.QRect(380, 60, 1300, 900))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(80, 60, 1161, 761))
        self.frame.resize(1140, 833)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(9, 9), blurRadius=100, color=QColor("black")
        )

        self.frame.setGraphicsEffect(effect)
        self.frame.setStyleSheet("background-color: #f8f8f8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(440, 70, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 841, 461))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(1, 690)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.LoadData = QtWidgets.QPushButton(self.frame, clicked=lambda: self.select_data())
        self.LoadData.setGeometry(QtCore.QRect(430, 640, 151, 28))
        self.LoadData.setObjectName("LoadData")

        self.tableWidget.raise_()
        self.label.raise_()
        self.LoadData.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def select_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='1230A', )
            cur = con.cursor()
            cur.execute('SELECT DISTINCT DATE(Date) FROM e_trainer.activity where idUser = %s;'
                        , (data[0]))
            Dates = cur.fetchall()
            self.tableWidget.rowCount()
            for row_number, row_data in enumerate(Dates):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(row_data[0])))
                cur = con.cursor()
                cur.execute('SELECT DISTINCT Exername FROM e_trainer.activity where Date = %s AND idUser = %s;'
                            , (row_data[0], data[0]))
                Activities = cur.fetchall()
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(str(', '.join(a[0] for a in Activities))))

        except Exception as es:
            print(es)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "History"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "What you practiced"))
        self.LoadData.setText(_translate("Form", "Load History Data"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
