import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

import yoga_Side_angel
import yoga_guerrier
from GUI import drawhint
a_thread = threading.Thread(target=yoga_Side_angel.main, args=())
a_thread.start()
print("dasda")
