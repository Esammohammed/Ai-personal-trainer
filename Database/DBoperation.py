import pymysql
from PyQt5.QtWidgets import QMessageBox
class database_operations:
    global con
    con = pymysql.connect(host='localhost', user='root', password='1234', )
    def select_user(id, password):


                cur = con.cursor()
                cur.execute('select * from e_trainer.userr where idUser=%s and password=%s'
                            , (id, password ))
                row = cur.fetchone()
                return row
    def insert (id , name ,email  , password ,age,height,weight ,level,gender):

        cur = con.cursor()
        cur.execute(
            "INSERT INTO `e_trainer`.`userr` (`idUser`, `name`, `Email`, `Password`, `Age`, `height`, `weight`, `Level`, `Gender`) "
            " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            , (id, name, email, password, age, height, weight, level, gender))
        con.commit()
        con.close()


    def test (self):
        print("aaa")
    def Update(id, name, email, password, age, height, weight, level, gender):
        try:

            cur = con.cursor()
            statment =  "UPDATE `e_trainer`.`userr` SET  `name` = %s, `Email` = %s, `Password` = %s, `Age` = %s, `height` = %s, `weight` = %s, `Level` = %s, `Gender` = %s WHERE (`idUser` = %s);"

            cur.execute(statment,( name, email, password, age, height, weight, level, gender, id) )
            con.commit()
            con.close()

        except Exception as es:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("")
            msg.setWindowTitle("")
            msg.exec_()

    def GetAchievements(id):

        cur = con.cursor()
        cur.execute('select * from e_trainer.bestscore where username=%s'
                    , (id))
        row = cur.fetchall()
        return row




