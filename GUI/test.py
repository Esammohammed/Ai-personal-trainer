from pyqt5_plugins.examplebutton import QtWidgets

import drawhint
exyogaFrame = QtWidgets.QFrame(centralwidget)
        self.exyogaFrame.setGeometry(QtCore.QRect(80, 60, 0, 0))

        self.exyogaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exyogaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exyogaFrame.setObjectName("exyogaFrame")

        ui = exercise_yoga.Ui_Frame()
        ui.setupUi(self.exyogaFrame)
        self.exyogaFrame.show()
        frame.hide()