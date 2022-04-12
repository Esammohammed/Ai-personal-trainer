import pymysql
from PyQt5.QtWidgets import QMessageBox
class User_info():
    id = ''
    name = ''
    email= ''
    password = ''
    age = ''
    height = ''
    weight =''
    level = ''
    gender = ''

    def select_user(id, password):
                con = pymysql.connect(host='localhost', user='root', password='1230A',
                                      )
                cur = con.cursor()
                cur.execute('select * from e_trainer.userr where idUser=%s and password=%s'
                            , (id, password ))
                row = cur.fetchone()
                id = row[0]
                name = row[1]
                email = row[2]
                password = row[3]
                age = row[4]
                height = row [5]
                weight =row [6]
                level = row [7]
                gender = row[8]
                return row
    def insert (id , name , password , age ,email,height,weight ,level,gender):
        con = pymysql.connect(host='localhost', user='root', password='1230A',)
        cur = con.cursor()
        cur.execute("INSERT INTO `e_trainer`.`userr` (`idUser`, `name`, `Email`, `Password`, `Age`, `height`, `weight`, `Level`, `Gender`) "
                    " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    , (id, name, email, password, age,height,weight ,level,gender ))
        con.commit()

        con.close()


