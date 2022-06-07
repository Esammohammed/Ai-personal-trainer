from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_Frame(object):
    exnum =''

    def YogaSAClicked(self):
        self.exnum = 'YSA'
        self.textBrowser.setText('What is this yoga pose ?\n'
                                 '-Side Angle Pose is a yoga pose that engages the legs, shoulders and abdominals.'
                                 ' This lengthening pose helps reduce stiffness in the shoulders and back, '
                                 'and it’s easily modifiable to accommodate varying levels of flexibility.\n'
                                 '\nHow to do it ?\n'
                                 '*Step 1*\n'
                                 '-Standing tall, position your legs in a wide parallel stance and raise your arms straight out at your sides.'
                                 ' Rotate your left leg outward so the center of your kneecap aligns with the center of your left ankle.'
                                 ' Bend the left knee and keep your right leg straight.\n'
                                 '*Step 2*\n'
                                 '-Lower your left hand to the floor in front of your left foot.'
                                 ' Raise your right arm overhead and lengthen the entire right side of your body,'
                                 ' gazing toward your extended arm. Repeat on the other side.\n'
                                 '\nWhat are the benefits of this pose?\n'
                                 '1-Leg Stretch.\n'
                                 '2-Core Strength.\n'
                                 '3-Full-body Strength.\n')

    def YogaGurrierClicked(self):
        self.exnum = 'YG'
        self.textBrowser.setText('What is this yoga pose ?\n'
                                 'Yoga gurriuer pose (Warrior II pose) is a physical, mental and emotional workout. '
                                 'As one of the most widely practiced postures in yoga, it’s suitable for yogis of all levels\n'
                                 '\nHow to do it ?\n'
                                 '1-The back foot points outward at 90 degrees.\n'
                                 '2-The outer side of the rear foot remains well on the ground, the leg is fully extended.\n'
                                 '3-The hips are facing outward.\n'
                                 '4-The front knee forms a right angle and a line with the ankle (whether seen from above or from the side).\n'
                                 '5-The upper body is centered over the hips and directed to the side.\n'
                                 '6-The navel is pulled towards the spine, the lower back is long, the pelvis is active.\n'
                                 '7-The shoulders are relaxed.\n'
                                 '8-The arms are stretched at the same level, they form a line.\n'
                                 '9-The gaze goes to the middle finger of the front hand.\n'
                                 '\n What are the benefits of this pose?\n'
                                 'This pose work nearly all your muscles. '
                                 'It strengthens your legs, glutes, hips, core, chest, shoulders and arms.'
                                 ' Holding the pose for an extended period of time will also help develop endurance.')

    def YogaCobraClicked(self):

        self.exnum = 'YCS'
        self.textBrowser.setText('What is this yoga pose ?\n'
                                 'It\'s a stretch pose that targets the hip flexors, which are the muscles along the front of the thigh and pelvis.\n'
                                 '\nHow to do it ?\n'
                                 '1- Start by lying flat on your stomach.\n'
                                 '2- Point your toes behind you and place your hands under your shoulders.\n'
                                 '3- Keep your elbows close to your ribs.\n'
                                 '4- Inhale and press your palms into the floor as you lift your chest off the ground.\n'
                                 '5- Slightly bend your elbows and hug them into your sides.\n'
                                 '6- Pull your belly in and roll your shoulders down and back.\n'
                                 '7- Keep your neck neutral and gaze upward.\n'
                                 '8- Exhale and return to start.\n'
                                 '\n What are the benefits of this exercise?\n'
                                 'It increases flexibility and strength in your back, arms, and shoulders.')


    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setGeometry(QtCore.QRect(80, 60, 1161, 761))
        self.centralwidget = QtWidgets.QWidget(Frame)
        self.centralwidget.setObjectName("centralwidget")
        Frame.resize(1140, 833)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)

        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1161, 111))
        self.frame_4.setStyleSheet("background-color: #f8f8f8;")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=50, color=QColor("black")
        )
        self.frame_4.setGraphicsEffect(effect)
        self.frame_4.setStyleSheet("background-color: #f8f8f8;")
        self.frame_4.resize(1140, 833)
        self.YSAButton = QtWidgets.QPushButton(self.frame_4)
        self.YSAButton.setGeometry(QtCore.QRect(110, 70, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.YSAButton.setFont(font)
        self.YSAButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ysa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.YSAButton.setIcon(icon2)
        self.YSAButton.setIconSize(QtCore.QSize(100, 100))
        self.YSAButton.setObjectName("YSAButton")
        self.YSAButton.clicked.connect(lambda :self.YogaSAClicked())

        self.YGButton = QtWidgets.QPushButton(self.frame_4)
        self.YGButton.setGeometry(QtCore.QRect(110, 170, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.YGButton.setFont(font)
        self.YGButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pushUp logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.YGButton.setIcon(icon1)
        self.YGButton.setIconSize(QtCore.QSize(100, 100))
        self.YGButton.setObjectName("YGButton")
        self.YGButton.clicked.connect(lambda :self.YogaGurrierClicked())

        self.YCSButton = QtWidgets.QPushButton(self.frame_4)
        self.YCSButton.setGeometry(QtCore.QRect(110, 270, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.YCSButton.setFont(font)
        self.YCSButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("shoulder press logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.YCSButton.setIcon(icon3)
        self.YCSButton.setIconSize(QtCore.QSize(100, 100))
        self.YCSButton.setObjectName("YCSButton")
        self.YCSButton.clicked.connect(lambda:self.YogaCobraClicked())

        self.textBrowser = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser.setGeometry(QtCore.QRect(380, 50, 641, 660))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)

        self.start = QtWidgets.QPushButton(self.frame_4)
        self.start.setGeometry(QtCore.QRect(110, 660, 221, 50))
        self.start.setStyleSheet(" ")

        self.start.setStyleSheet("QPushButton{color : white ;background-color: #04AA6D!important;border-radius: 5px;font-size: 17px; "
                                 "font-family: 'Source Sans Pro', sans-serif;padding: 6px 18px;font-weight: bold}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #059861;\n"
                                 "}")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setLayoutDirection(QtCore.Qt.LeftToRight)
        'icon = QtGui.QIcon()'
        'icon.addPixmap(QtGui.QPixmap("squat logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)'

        self.start.setObjectName("startButton")
        self.start.clicked.connect(lambda: Startexercise(self.exnum))

        self.retranslateUi(self.frame_4)
        QtCore.QMetaObject.connectSlotsByName(self.frame_4)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.YSAButton.setText(_translate("Frame", "Side Angel"))
        self.YGButton.setText(_translate("Frame", "Warrior Pose"))
        self.YCSButton.setText(_translate("Frame", "Cobra Stretch"))
        self.start.setText(_translate("Frame", "Start"))
def Startexercise (exnum):
    print (exnum)

    if exnum=='YSA' :
        import yoga_Side_angel
        yoga_Side_angel.main()
    if exnum =='YG':
        import yoga_guerrier
        yoga_guerrier.main()
    if exnum == 'YCS':
        import yoga_stretch
        yoga_stretch.main()

if __name__ == "__main__":
    import sys
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()