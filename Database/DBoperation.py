import pymysql
from PyQt5.QtWidgets import QMessageBox
class User_info:

    def select_user(id, password):
                con = pymysql.connect(host='localhost', user='root', password='1230A',
                                      )
                cur = con.cursor()
                cur.execute('select * from e_trainer.userr where idUser=%s and password=%s'
                            , (id, password ))
                row = cur.fetchone()
                return row
    def insert (id , name ,email  , password ,age,height,weight ,level,gender):
        con = pymysql.connect(host='localhost', user='root', password='1230A',)
        cur = con.cursor()
        cur.execute("INSERT INTO `e_trainer`.`userr` (`idUser`, `name`, `Email`, `Password`, `Age`, `height`, `weight`, `Level`, `Gender`) "
                    " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    , (id, name, email, password, age,height,weight ,level,gender ))
        con.commit()

        con.close()


