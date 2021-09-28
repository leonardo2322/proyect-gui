import tkinter as tk
from tkinter import ttk, messagebox as mb
import class_frame_1
import frma_2
from PIL import Image


class application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg="light grey")
        self.title("Administrador")
        self.geometry("1360x1000")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        contenedor1 = tk.Frame(self, bg="light grey")
        contenedor1.grid(padx=5, pady=5, sticky="nsew")

        menubar = tk.Menu(contenedor1)
        self.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Guadar")

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Borrar")

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Editar", menu=editmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        self.todos_los_frames = dict()

        for F in (class_frame_1.frame_1, frma_2.frame_2):

            frame = F(contenedor1, self)
            self.todos_los_frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(class_frame_1.frame_1)

    def show_frame(self, contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()
        return frame

    def salir(self, container, controller):
        valor = mb.askquestion("Salir", "Deseas salir de la Aplicacion yeny")
        if valor == "yes":
            return container.destroy(), controller.destroy()


# -------------------Barra Menu


if __name__ == "__main__":
    root = application()
    root.mainloop()
