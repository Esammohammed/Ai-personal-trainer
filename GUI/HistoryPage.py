
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
data = ('1', '2', '3', '4', None, None, None, None, None)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000, 1000)
        self.frame = QtWidgets.QFrame(Form)


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

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()



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
        self.LoadData = QtWidgets.QPushButton(self.frame)
        self.LoadData.setGeometry(QtCore.QRect(430, 640, 151, 28))
        self.LoadData.setObjectName("LoadData")
        self.LoadData.clicked.connect(self.select_data)
        self.tableWidget.raise_()
        self.label.raise_()
        self.LoadData.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def Create_table(self ,user_rows):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(user_rows)
        for i in range(user_rows):
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
            _translate = QtCore.QCoreApplication.translate
            item = self.tableWidget.verticalHeaderItem(0)
            item.setText(_translate("Form", "1"))

    def select_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='1230A', )
            cur = con.cursor()
            cur.execute('SELECT DATE(Date) FROM e_trainer.activity where idUser = %s group by Date;'
                        , 5)
            Dates = cur.fetchall()
            self.tableWidget.rowCount()
            for row_number, row_data in enumerate(Dates):
               self.tableWidget.insertRow(row_number)
               for column_number, Itemdata in enumerate(row_data):
                 self.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(Itemdata)))


            for date in Dates:
                cur.execute('SELECT Exername FROM e_trainer.activity where Date = %s;'
                            , (date[0]))
                Activities = cur.fetchall()
                self.tableWidget.rowCount()
                for row_number, row_data in enumerate(Activities):
                    self.tableWidget.insertRow(row_number)
                    for column_number, Itemdata in enumerate(row_data):
                        self.tableWidget.setItem(row_number, 1, QTableWidgetItem(str(Itemdata)))
        except Exception as es:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "History"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Form", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Form", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Form", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Form", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Form", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Form", "20"))
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
