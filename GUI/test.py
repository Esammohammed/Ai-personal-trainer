import pymysql

con = pymysql.connect(host="localhost", user="root", password="1230A"  )

cur = con.cursor()

cur.execute("INSERT INTO `e_trainer`.`userr` (`idUser`, `name`, `Email`, `Password`) values(%s,%s,%s,%s)"

                                , (2 ,2, 2,2))

con.commit()
con.close()