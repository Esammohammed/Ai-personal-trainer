from datetime import datetime

import cv2

import Shoulder_Press
import bicepscurl
import lateral_raises
import squat
import push_up
import yoga_Side_angel
import yoga_guerrier
import yoga_stretch


def Startex(Exersicename,ui,filepath):
    if (filepath==''):
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(filepath)

    if Exersicename == 'bicepscurl':
        bicepscurl.main(ui,cap)
    if Exersicename == 'lateral raises':
        lateral_raises.main(ui,cap)
    if Exersicename =='squat':
        squat.main(ui,cap)
    if Exersicename == 'shoulder_press':
        Shoulder_Press.main()
    if Exersicename == 'pushup':
        push_up.main()
    if Exersicename == 'Yoga side angle':
       yoga_Side_angel.main(ui,cap)
    if Exersicename == 'Yoga Guerrier':
      yoga_guerrier.main(ui,cap)
    if Exersicename == 'Yoga stretch':
        yoga_stretch.main(ui,cap)

