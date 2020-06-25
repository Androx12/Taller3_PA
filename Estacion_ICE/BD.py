import sqlite3 as Obj_SQL
from sqlite3 import Error

class BD:

    def __init__(self):
        pass


    def SQLLite_Create_DB(self): #Crear BD y abrir conexion
        try:
            Conexion = Obj_SQL.connect('BD_EstacionICE.db')
            return Conexion
        except Error as Err:
            print ('Ocurrio un error: ',Err)


    def Create_table(self, connetion): #Crear tabla con un Identity (AUTOINCREMENT)
        try:
            cursor = connetion.cursor()
            cursor.execute("CREATE TABLE T_Operario(_id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT)")
            connetion.commit()
        except Error as Err:
            print ('Ocurrio un error: ',Err)


    def Insertar_New_Row(self, connetion, Valor): #Insertar valores en BD solo se envía un valor en forma de lista
        try:
            cursor = connetion.cursor()
            cursor.execute("INSERT INTO T_Operario(Nombre) VALUES(?)", Valor)
            connetion.commit()
        except Error as Err:
            print ('Ocurrio un error: ',Err)


    def Get_All_Rows(self, connetion): #Realizar un Select a la tabla
        try:
            cursor = connetion.cursor()
            cursor.execute("SELECT * FROM T_Operario")
            Objeto_Resultado = cursor.fetchall()
            connetion.commit()
            return Objeto_Resultado

        except Error as Err:
            Err


    def ProcesoDB (self):   #Se cra un proceso que se encrgue de la logica del BD
        
        Obj_Conexion = self.SQLLite_Create_DB()     #Se obtiene la conexión y realizamos un Select para verificar
        Resultado = self.Get_All_Rows(Obj_Conexion) #si existe información en la tabla guardamos el resultado

        if Resultado:       #Si el resultado EXISTE obtenemos la información de BD y la retornamos
            if Resultado:
                for Item in Resultado:
                    Resultado = self.Get_All_Rows(Obj_Conexion)
                    return Resultado
            else:
                return Resultado
        else:               #Si el resultado NO EXISTE procedemos a crear la tabla
            self.Create_table(Obj_Conexion)
            Resultado = self.Get_All_Rows(Obj_Conexion)
            return Resultado