import sqlite3

class basedate():
    def  __init__(self):
        self.conexion = sqlite3.connect("DB_1.db")
        self.cursor = self.conexion.cursor()

    def llenar_registros(self,user,contra,tipo):
        self.cursor.execute("Insert into usuarios (nombre,pass,tipo_user) values ($,$,$)",[user,contra,tipo])
        self.conexion.commit()
        self.conexion.close()



    def consultas_log(self,user,contra):
        self.cursor.execute("Select * from usuarios where nombre=$usuario and pass=$contra",(user,contra))
        resul = self.cursor.fetchall()
        #verificar si regresa  algo o no
        if len(resul)>0:
            if resul[0][1] == user and resul[0][2] == contra:
                return True
            else:
                return False
        else:
            return False
        self.conexion.close()