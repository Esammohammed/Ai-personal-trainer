import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from GUI import  exercise_info

Form = QtWidgets.QWidget()
ui = exercise_info.Ui_Frame()
ui.setupUi(Form)
Form.show()

