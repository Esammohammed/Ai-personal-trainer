from datetime import datetime

import Shoulder_Press
import bicepscurl
import lateral_raises
import squat
import push_up
import yoga_Side_angel
import yoga_guerrier
import yoga_stretch

Trainingname = ''
Rmtime = datetime.now()
Repscount = 0
def Startex(Exersicename,ui):
    if Exersicename == 'bicepscurl':
        bicepscurl.main(ui)
    if Exersicename == 'lateral raises':
        lateral_raises.main(ui)
    if Exersicename =='squat':
        squat.main(ui)
    if Exersicename == 'shoulder_press':
        Shoulder_Press.main()
    if Exersicename == 'pushup':
        push_up.main()
    if Exersicename == 'Yoga side angle':
       yoga_Side_angel.main(ui)
    if Exersicename == 'Yoga Guerrier':
      yoga_guerrier.main(ui)
    if Exersicename == 'Yoga stretch':
        yoga_stretch.main(ui)

