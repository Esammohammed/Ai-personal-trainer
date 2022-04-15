import pymysql

con = pymysql.connect(host='localhost', user='root', password='1230A', )
cur = con.cursor()
cur.execute('SELECT DATE(Date) FROM e_trainer.activity where idUser = %s group by Date;'
            , (5))
Dates = cur.fetchall()

for date in Dates:
    print (date[0])
    cur.execute('SELECT Exername FROM e_trainer.activity where Date = %s;'
                , (date[0]))
    Activities = cur.fetchall()
    print (Activities)

