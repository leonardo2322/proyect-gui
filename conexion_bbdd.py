import sqlite3
# base de datos de la aplicacion gui whoami
from tkinter import messagebox as mb


class Basedata:

    def __init__(self, conexion_base, unalista):
        self.conexion = conexion_base
        self.curso()

    def curso(self):
        try:
            mi_cursor = self.conexion.cursor()
            mi_cursor.execute("""
                CREATE TABLE  ADMINISTACION(FECHA DATE PRIMARY KEY ,
                 ESPECIFICACION VARCHAR(50), GASTOS INTEGER(20),
                  INGRESOS INTEGER(20))""")
            mi_cursor.close()
            mb.showinfo("base datos", "ya hay un base de datos")
        except sqlite3.OperationalError:
            print("ok")
        self.conexion.commit()
        self.conexion.close()
        self.lista = []

    def con(self, lista):
        miconexion = sqlite3.connect("base_datos_Gui")
        cursor = miconexion.cursor
        cursor.execute("INSERT INTO ADMINISTRACION VALUES")


