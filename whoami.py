from tkinter import *
from tkinter import messagebox
import sys
import os

# clase padre


class application:
    def __init__(self):

        self.master = Tk()
        self.frame = Frame(self.master)
        self.frame.grid()
        self.master.title("Python files")
        self.master.geometry("500x300")
        self.botones()
        self.labels()
        self.barmenu()
        self.entryes()

    # Barra Menu

    def barmenu(self):
        barramenu = Menu(self.master)
        self.master.config(menu=barramenu, width=300, height=300)
        ArchiveMenu = Menu(barramenu)
        ArchiveSettings = Menu(barramenu)
        ArchiveHelp = Menu(barramenu)
        ArchiveEdicion = Menu(barramenu)
        barramenu.add_cascade(label="Archivo", menu=ArchiveMenu)
        barramenu.add_cascade(label="Herramientas", menu=ArchiveSettings)
        barramenu.add_cascade(label="Ayuda", menu=ArchiveHelp)
        barramenu.add_cascade(label="Edicion", menu=ArchiveEdicion)

    # Texto de especificacion del campo

    def labels(self):
        label1 = Label(self.frame, text="Fecha")
        label1.grid(row=0, column=0, padx=5, pady=5)
        label1.config(fg="blue", font=("Verdana", 14), bg="light grey")

        label2 = Label(self.frame, text="Especificaciones")
        label2.grid(row=0, column=1, padx=5, pady=5)
        label2.config(fg="black", font=("Verdana", 14), bg="light grey")

        label3 = Label(self.frame, text="Gastos")
        label3.grid(row=0, column=2, padx=5, pady=5)
        label3.config(fg="red", font=("Verdana", 14), bg="light grey")

        label4 = Label(self.frame, text="Ingresos")
        label4.grid(row=0, column=3, padx=5, pady=5)
        label4.config(fg="green", font=("Verdana", 14), bg="light grey")

    # Entradas de texto

    def entryes(self):
        entrada1 = Entry(self.frame, width=12)
        entrada1.grid(row=1, column=0, padx=2, pady=5)
        entrada2 = Entry(self.frame, width=30)
        entrada2.grid(row=1, column=1, padx=0, pady=2)
        entrada3 = Entry(self.frame, width=12)
        entrada3.grid(row=1, column=2, padx=0, pady=2)
        entrada4 = Entry(self.frame, width=15)
        entrada4.grid(row=1, column=3, padx=0, pady=2)

    # iniciar tk la ventana

    def iniciar(self):
        return self.master.mainloop()

    # botones de funcionalidad

    def botones(self):
        boton = Button(self.frame, text="Guardar")
        boton.grid(row=2, column=1)
        boton1 = Button(self.frame, text="Borrar")
        boton1.grid(row=2, column=2)
        boton2 = Button(self.frame, text="Salir", command=salir())
        boton2.grid(row=2, column=3)
        boton3 = Button(self.frame, text="Mostrar")
        boton3.grid(row=2, column=0)

        def salir(self):
            return self.master.destroy()
    # funcion principal


def main():
    root = application()

    root.iniciar()


if __name__ == "__main__":
    main()
