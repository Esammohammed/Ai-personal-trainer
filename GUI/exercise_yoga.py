
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from GUI import exercise2


class Ui_Frame(object):
    exnum =''
    def bicepsClicked(self):

        self.exnum = 'biceps'
        self.textBrowser.setText('What are used muscles for this exercise ?\n'
                                 '-This exercise is for The biceps or biceps brachii muscle which is a large muscle that lies on the front of the upper arm between the shoulder and the elbow.\n'
                                 '\nHow to do it ?\n'
                                 '-With a dumbbell in hand, slowly curl the dumbbell upward at a controlled tempo,'
                                 ' concentrating on contracting the biceps to move the load.'
                                 'At the top of the movement, flex as hard as possible, then slowly lower the load.\n'
                                 '*The key is not to lose tension on the biceps at any point in the range of motion.*\n'
                                 '\nWhat are the benefits of this exercise?\n'
                                 '-Apart from building muscle size, boosting athletic performance and facilitating daily activities, bicep curls build strength in the upper arm, train shoulder to be more stable.')

    def back(self):
        ui = exercise2.Ui_MainWindow()
        ui.setupUi(self.exFrame)
        self.exFrame.show()
        self.hisframe.hide()
        self.achFrame.hide()
        self.usFrame.hide()
    def pushUpClicked(self):
        self.exnum = 'pushup'
        self.textBrowser.setText('What are used muscles for this exercise ?\n'
                                 'Targets are Chest, arms, shoulders, and core\n'
                                 '\nHow to do it ?\n'
                                 'Get on the floor on all fours, positioning your hands slightly wider than your '
                                 'shoulders. Don\'t lock out the elbows; keep them slightly bent. Extend your legs '
                                 'back so you are balanced on your hands and toes, your feet hip-width apart.'
                                 '\n1- Contract your abs and tighten your core by pulling your belly button toward your spine.'
                                 '\n2- Inhale as you slowly bend your elbows and lower yourself to the floor, until your elbows are at a 90-degree angle.'
                                 '\n3- Exhale while contracting your chest muscles and pushing back up through your hands, returning to the start position.\n'
                                 '\n What are the benefits of this exercise?\n'
                                 '1. Increase Functional Strength via Full Body Activation\n'
                                 '2. Muscle Stretching for Health and Vitality\n'
                                 '3. Enhance Your Cardiovascular System\n'
                                 '4. Increase Whole Body Muscle Definition – HGH Promotion\n'
                                 '5. Protect Your Shoulders from Injury\n'
                                 '6. Improve Your Posture\n'
                                 '7. Prevent Lower Back Injuries\n')

    def shoulderPressClicked(self):

        self.exnum = 'ysa'
        self.textBrowser.setText('What are used muscles for this exercise ?\n'
                                 'pectorals (chest), deltoids (shoulders),triceps (arms) and trapezius (upper back)\n'
                                 '\nHow to do it ?\n'
                                 'Hold the dumbbells by your shoulders with your palms facing forwards and your elbows out to the sides and bent at a 90° angle.'
                                 ' Without leaning back, extend through your elbows to press the weights above your head. Then slowly return to the starting position.\n'
                                 '\n What are the benefits of this exercise?\n'
                                 '1- strength and size of the shoulder muscles\n'
                                 '2- strength and size of the triceps muscles\n'
                                 '3- strength and size of the trapezius muscle\n'
                                 '4- strength in the core muscles, such as your obliques, transverse abdominal muscles, lower back, and spinal stabilizers, when performing the exercise while standing\n'
                                 '5- improve performance of other exercises, like the bench press\n')

    def bicepsClicked(self):

        self.exnum = 'ysa'
        self.textBrowser.setText('What are used muscles for this exercise ?\n'
                                 'A lateral raise works your shoulder muscles as well as your triceps.\n'
                                 '\nHow to do it ?\n'
                                 'Stand or sit with a dumbbell in each hand at your sides.'
                                 ' Keep your back straight, brace your core,'
                                 ' and then slowly lift the weights out to the side until your arms are parallel with the floor, '
                                 'with the elbow slightly bent. Then lower them back down, '
                                 'again in measured fashion – you’ll find it all the harder if you avoid speeding up. '
                                 'A lot of people will cheat by “shrugging” the weights up using their traps.'
                                 ' Resist the urge to do that by not raising your shoulder blades during the rep – instead focus on the delts\n'
                                 '\n What are the benefits of this exercise?\n'
                                 'Strengthening your shoulder and upper back muscles helps build strength in your rear deltoids and upper body.'
                                 ' On an aesthetic level, strong deltoids will help your upper body look bigger, stronger, and more toned.\n')



    def squatClicked(self):
        self.exnum = 'ysa'
        self.textBrowser.setText('What are used muscles for this exercise ?\n'
                                 'The primary muscles involved include the gluteus maximus, hip flexors, and quadriceps.\n'
                                 '\nHow to do it ?\n'
                                 '1- Stand straight with feet hip-width apart.\n'
                                 '2- Tighten your stomach muscles.\n'
                                 '3- Lower down, as if sitting in an invisible chair.\n'
                                 '4- Straighten your legs to lift back up.\n'
                                 '5- Repeat the movement again and again.\n'
                                 '\n What are the benefits of this exercise?\n'
                                 'Squats burn calories and might help you lose weight.'
                                 'They also lower your chances of injuring your knees and ankles. As you exercise,'
                                 'the movement strengthens your tendons, bones, and ligaments around the leg muscles.\n'
                                 'there are muscles that benefit from squats, too like Hip muscles, Calves, Hamstrings and Obliques.')


    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1140, 833)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=50, color=QColor("black")
        )
        Frame.setGraphicsEffect(effect)
        Frame.setStyleSheet("background-color: #f8f8f8;")

        self.pushUpButton = QtWidgets.QPushButton(Frame)
        self.pushUpButton.setGeometry(QtCore.QRect(110, 100, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushUpButton.setFont(font)
        self.pushUpButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("warrior.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushUpButton.setIcon(icon1)
        self.pushUpButton.setIconSize(QtCore.QSize(100, 100))
        self.pushUpButton.setObjectName("pushUpButton")
        self.pushUpButton.clicked.connect(lambda :self.pushUpClicked())
        self.bicepsButton = QtWidgets.QPushButton(Frame)
        self.bicepsButton.setGeometry(QtCore.QRect(110, 250, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bicepsButton.setFont(font)
        self.bicepsButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ysa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bicepsButton.setIcon(icon2)
        self.bicepsButton.setIconSize(QtCore.QSize(100, 100))
        self.bicepsButton.setObjectName("bicepsButton")
        self.bicepsButton.clicked.connect(lambda :self.bicepsClicked())
        self.shoulderPressButton = QtWidgets.QPushButton(Frame)
        self.shoulderPressButton.setGeometry(QtCore.QRect(110, 400, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shoulderPressButton.setFont(font)
        self.shoulderPressButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("cobra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoulderPressButton.setIcon(icon3)
        self.shoulderPressButton.setIconSize(QtCore.QSize(100, 100))
        self.shoulderPressButton.setObjectName("shoulderPressButton")
        self.shoulderPressButton.clicked.connect(lambda:self.shoulderPressClicked())

        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(380, 50, 641, 660))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)


        self.start = QtWidgets.QPushButton(Frame)
        self.start.setGeometry(QtCore.QRect(110, 660, 221, 50))
        self.start.setStyleSheet(" ")

        self.start.setStyleSheet("QPushButton{color : white ;background-color: #04AA6D!important;border-radius: 5px;font-size: 17px; "
                                 "font-family: 'Source Sans Pro', sans-serif;padding: 6px 18px;font-weight: bold}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #059861;\n"
                                 "}")
        self.start.clicked.connect(lambda: Startexercise(self.exnum))
        self.back = QtWidgets.QPushButton(Frame)
        self.back.setGeometry(QtCore.QRect(110, 720, 221, 50))
        self.back.setStyleSheet(" ")

        self.back.setStyleSheet("QPushButton{\n"
                                "background-color:#2b3942;\n"
                                "color:white;\n;border-radius: 5px;font-size: 17px; "
                                "font-family: 'Source Sans Pro', sans-serif;padding: 6px 18px;font-weight: bold}\n"

                                "\n"
                                "QPushButton:hover {\n"
                                "  background-color: #1f292f;\n"
                                "}")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back.clicked.connect(lambda: self.back)
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))

        self.pushUpButton.setText(_translate("Frame", "Warrior Pose"))
        self.bicepsButton.setText(_translate("Frame", "Side Angel"))
        self.shoulderPressButton.setText(_translate("Frame", "Cobra Stretch"))

        self.start.setText(_translate("Frame", "Start"))
        self.back.setText(_translate("Frame", "Back"))

def Startexercise (exnum):
    print (exnum)

    if exnum=='ysa' :
        import yoga_Side_angel
        yoga_Side_angel.main()

if __name__ == "__main__":
    import sys
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
