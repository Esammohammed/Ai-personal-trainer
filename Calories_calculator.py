from datetime import datetime


def Cl_cal (Exersicename, reps , time):
    time = str(time)
    d = datetime.strptime(time, "%H:%M:%S")
    Timeinmins= d.minute+(d.second/60)
    caloriesburned = 0.0
    ex_info=''
    if Exersicename == 'bicepscurl':
        caloriesburned= .11 *reps;
        ex_info='Bicep curl burns average .11 calories per rep'

    if Exersicename == 'lateral raises':
        caloriesburned =(Timeinmins/10)*100
        ex_info = 'Lateral Raises 10-minute-session helps you burn 100 calories'


    if Exersicename =='squat':
        caloriesburned = .32 * reps;
        ex_info = 'One Squat burns 0.32 calorie which means you have to do 100 squat to burn 32 calories'

    if Exersicename == 'shoulder press':
        caloriesburned = 4 * reps;
        ex_info = '10 minutes exercising shoulder press help you burns 36 Calories'
    if Exersicename == 'push up':
        caloriesburned = .35 * reps;
        ex_info = 'pushups can burn at least 7 caloriesTrusted Source per minutes'
    if Exersicename == 'Yoga side angle':
        caloriesburned = (Timeinmins/60) * 477;
        ex_info = 'Yoga side angle helps you burn 477 calories in an hour'

    if Exersicename == 'Yoga Guerrier':
        caloriesburned = (Timeinmins/60) * 189
        ex_info = 'Yoga guerrier helps you burn 189 calories for each one-hour session'

    if Exersicename == 'Yoga stretch':
        caloriesburned = (Timeinmins/60) * 300
        ex_info = 'For a 60-minute yoga class, that would add up to 216–426 calories'

    return round(caloriesburned,2), ex_info