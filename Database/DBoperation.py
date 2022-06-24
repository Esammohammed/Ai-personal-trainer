import pymysql
from PyQt5.QtWidgets import QMessageBox
class database_operations:
    global con
    con = pymysql.connect(host='localhost', user='root', password='1230A', )
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
        con = pymysql.connect(host='localhost', user='root', password='1230A', )
        cur = con.cursor()
        cur.execute('select * from e_trainer.bestscore where username=%s'
                    , (id))
        row = cur.fetchall()

        con.close()
        return row



    def insertBestScore(exerciseName, id, newscore, extype):
        cur = con.cursor()
        cur.execute('select * from e_trainer.bestscore where username=%s and exename=%s'
                    , (id, exerciseName))
        row = cur.fetchone()
        if (row == None):
            cur = con.cursor()
            cur.execute(
                "INSERT INTO e_trainer.bestscore (exename, username, bestscore, exType)"
                " values(%s,%s,%s,%s)"
                , (exerciseName, id, newscore, extype))
            con.commit()
            con.close()
        elif (row[3]== 'work'):
            bestscore = row[2]

            if (str(newscore) >= bestscore):
                cur = con.cursor()
                statment = "UPDATE `e_trainer`.`bestscore` SET `bestscore` =  %s  WHERE (`username` =  %s) and (`exename` =  %s);"
                cur.execute(statment, (newscore, id, exerciseName))
            con.commit()
            con.close()


        else :
            pass




