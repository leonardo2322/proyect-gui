

from tkinter import ttk, PhotoImage, messagebox as mb
import tkinter as tk
from frma_2 import frame_2
from tkinter import Canvas
import sqlite3
import os

conexion = sqlite3.connect("base_datos_Gui")


class frame_1(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="light grey")
        self.datos = []
        self.img = PhotoImage(file="joys.png")
        self.imglabel = tk.Label(self, image=self.img)
        self.imglabel.grid(row=0, column=0)
        self.conectar = Basedata(conexion, self.datos)

# --------------VARIABLES DE ENTRYES--------------------------
        self.entrada0 = tk.IntVar()
        self.entrada1 = tk.StringVar()

        self.entrada2 = tk.StringVar()

        self.entrada3 = tk.IntVar()

        self.entrada4 = tk.IntVar()

# ----------------------entryes-------------------------------------------
        e_0 = ttk.Entry(self, width=10, textvariable=self.entrada0)
        e_0.grid(row=1, column=0, padx=5, pady=5)
        e_1 = ttk.Entry(self, width=10, textvariable=self.entrada1)
        e_1.grid(row=1, column=1, padx=5, pady=5)
        e_2 = ttk.Entry(self, width=30, textvariable=self.entrada2)
        e_2.grid(row=1, column=2, padx=5, pady=5)
        e_3 = ttk.Entry(self, width=10, textvariable=self.entrada3)
        e_3.grid(row=1, column=3, padx=5, pady=5)
        e_4 = ttk.Entry(self, width=10, textvariable=self.entrada4)
        e_4.grid(row=1, column=4, padx=5, pady=5)


# ----------------------buttons---------------------------------------------

        b_1 = tk.Button(self, text="Eliminar", bd=5)
        b_1.grid(row=2, column=5, padx=10, pady=10)
        b_2 = tk.Button(self, text="cambio_frame2", bd=5,
                        command=lambda: controller.show_frame(frame_2))
        b_2.grid(row=2, column=1, padx=10, pady=10)

        b_3 = tk.Button(self, text="Guardar", bd=5,
                        command=lambda: frame_1.Guardar(self, self.entrada0, self.entrada1, self.entrada2,
                                                        self.entrada3, self.entrada4, self.datos, self.conectar))

        b_3.grid(row=2, column=2, padx=10, pady=10)

        b_4 = tk.Button(self, text="Limpiar", bd=5,
                        command=lambda: limpiar(self))

        b_4.grid(row=2, column=3, padx=10, pady=10)

        self.b_5 = tk.Button(self, text="Salir", bd=5,
                             command=lambda: controller.salir(container, controller))

        self.b_5.grid(row=2, column=4, padx=10, pady=10)


# -----------------------labels------------------------------
        l_1 = ttk.Label(self, text="Fecha")
        l_1.grid(row=0, column=1, padx=10, pady=10)

        l_2 = ttk.Label(self, text="Especificacion")
        l_2.grid(row=0, column=2, padx=10, pady=10)

        l_3 = ttk.Label(self, text="Gastos")
        l_3.grid(row=0, column=3, padx=10, pady=10)

        l_4 = ttk.Label(self, text="Ingresos")
        l_4.grid(row=0, column=4, padx=10, pady=10)

# -----------funciones-------------------
        def limpiar(self):

            self.entrada1.set("")
            self.entrada2.set("")
            self.entrada3.set("")
            self.entrada4.set("")

    def Guardar(self, entrada0, entrada1, entrada2, entrada3, entrada4, lista2, llamada):

        self.datos = lista2
        self.cone = llamada
        try:
            entrada0 = self.entrada0.get()
            entrada1 = self.entrada1.get()
            entrada2 = self.entrada2.get()
            entrada3 = self.entrada3.get()
            entrada4 = self.entrada4.get()
            if entrada0 == (" ") and entrada1 == " " and entrada2 == " " and entrada3 == " " and entrada4 == " ":
                mb.showerror("Error", "No Rellenaste todos los campos")
            else:

                self.datos.append(entrada0)
                self.datos.append(entrada1)
                self.datos.append(entrada2)
                self.datos.append(entrada3)
                self.datos.append(entrada4)
                return self.cone.con(self.datos)

        except:
            mb.showwarning("Error", "No introdujiste ningun valor")


# -----------------------conexion y creacion de la base datos


class Basedata:

    def __init__(self, conexion_base, unalista):
        self.conexion = conexion_base
        self.curso()
        self.parametros = unalista
        self.con(self.parametros)

    def curso(self):
        try:
            mi_cursor = self.conexion.cursor()
            mi_cursor.execute("""
                CREATE TABLE ADMINISTACION(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                FECHA DATE,
                ESPECIFICACION VARCHAR(50),
                GASTOS INTEGER(20),
                INGRESOS INTEGER(20))""")
            mi_cursor.close()
            mb.showinfo("base datos", "ya hay un base de datos")
        except sqlite3.OperationalError:
            print("ok")
        self.conexion.commit()
        self.conexion.close()
        self.lista = []

    def con(self, lista):
        estlist = lista
        miconexion = sqlite3.connect("base_datos_Gui")
        cursor = miconexion.cursor()
        print(estlist)
        try:
            cursor.execute(
                """INSERT INTO ADMINISTACION VALUES(?,?,?,?,?)""", estlist)
            miconexion.commit()
            miconexion.close()
        except:
            print("no hay datos")

    def borrar(self, entr):
        miconexion = sqlite3.connect("base_datos_Gui")
        cursor = miconexion.cursor()
        cursor.execute(
            """DELETE FROM ADMINISTRACION WHERE ID=""")
        pass
