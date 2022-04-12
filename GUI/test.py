import pymysql

con = pymysql.connect(host="localhost", user="root", password="1230A"  )

cur = con.cursor()


cur.execute('select * from e_trainer.userr where idUser=%s and password=%s'  , (102, 4 ))

row = cur.fetchone()

