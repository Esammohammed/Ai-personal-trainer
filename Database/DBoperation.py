import pymysql
from PyQt5.QtWidgets import QMessageBox
class database_operations:

    def select_user(id, password):
                con = pymysql.connect(host='localhost', user='root', password='1230A',)

                cur = con.cursor()
                cur.execute('select * from e_trainer.userr where idUser=%s and password=%s'
                            , (id, password ))
                row = cur.fetchone()
                return row
    def insert (id , name ,email  , password ,age,height,weight ,level,gender):
        con = pymysql.connect(host='localhost', user='root', password='1230A', )
        cur = con.cursor()
        cur.execute("INSERT INTO `e_trainer`.`userr` (`idUser`, `name`, `Email`, `Password`, `Age`, `height`, `weight`, `Level`, `Gender`) "
                    " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    , (id, name, email, password, age,height,weight ,level,gender ))
        con.commit()

        con.close()
    def test (self):
        print("aaa")
    def Update(id, name, email, password, age, height, weight, level, gender):
        try:
            con = pymysql.connect(host='localhost', user='root', password='1230A',)
            cur = con.cursor()
            cur.execute(
                "UPDATE `e_trainer`.`userr` SET  `name` = '22', `Email` = '2', `Password` = '2', `Age` = '2', `height` = '2', `weight` = '22', `Level` = '2', `Gender` = '2' WHERE (`idUser` = '2');"
                 )
            con.commit()

            con.close()
        except Exception as es:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("")
            msg.setWindowTitle("")
            msg.exec_()

    def GetAchievements(id):
        con = pymysql.connect(host='localhost', user='root', password='1234', )

        cur = con.cursor()
        cur.execute('select * from e_trainer.bestscore where username=%s'
                    , (id))
        row = cur.fetchall()
        return row




