
import class_frame_1
from tkinter import ttk, PhotoImage, messagebox
import tkinter as tk


class frame_2(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="light grey")
        #self.img = PhotoImage(file="joys.png")
        #self.imglabel = tk.Label(self, image=self.img)
        #self.imglabel.grid(row=0, column=4, padx=1, pady=1)

        fram = tk.Frame(self, bg="light blue")
        fram.grid(row=8, column=4)
        fram.config(width=800, height=700)
        # ---------------botones-----------------------------------------
        b_1 = tk.Button(self, text="frame1", bd=5,
                        command=lambda: controller.show_frame(class_frame_1.frame_1))
        b_1.grid(row=6, column=3)

        b_2 = tk.Button(fram, text="Salon", bd=5)
        b_2.grid(row=8, column=0, ipadx=7, ipady=10, padx=5, pady=5)

        b_3 = tk.Button(fram, text="Bandejas", bd=5)
        b_3.grid(row=8, column=1, ipadx=7, ipady=10, padx=5, pady=5)

        b_4 = tk.Button(fram, text="Sencillos", bd=5)
        b_4.grid(row=8, column=2, ipadx=7, ipady=10, padx=5, pady=5)

        b_5 = tk.Button(fram, text="Platos Especiales", bd=5)
        b_5.grid(row=8, column=3, ipadx=7, ipady=10, padx=5, pady=5)

        b_6 = tk.Button(fram, text="Jugos", bd=5)
        b_6.grid(row=9, column=0, ipadx=7, ipady=10, padx=5, pady=5)

        b_7 = tk.Button(fram, text="Porciones", bd=5)
        b_7.grid(row=9, column=1, ipadx=7, ipady=10, padx=5, pady=5)

# ---------------------botones de las mesas---------------------

        mesa1 = tk.Button(fram, text="mesa1", bd=5)
        mesa1.grid(row=10, column=0, ipadx=7, ipady=10, padx=5, pady=5)

        mesa2 = tk.Button(fram, text="mesa2", bd=5)
        mesa2.grid(row=10, column=1, ipadx=7, ipady=10, padx=5, pady=5)

        mesa3 = tk.Button(fram, text="mesa3", bd=5)
        mesa3.grid(row=10, column=2, ipadx=7, ipady=10, padx=5, pady=5)

        mesa4 = tk.Button(fram, text="mesa4", bd=5)
        mesa4.grid(row=10, column=3, ipadx=7, ipady=10, padx=5, pady=5)

        mesa5 = tk.Button(fram, text="mesa5", bd=5)
        mesa5.grid(row=11, column=0, ipadx=7, ipady=10, padx=5, pady=5)

        mesa6 = tk.Button(fram, text="mesa6", bd=5)
        mesa6.grid(row=11, column=1, ipadx=7, ipady=10, padx=5, pady=5)

        mesa7 = tk.Button(fram, text="mesa7", bd=5)
        mesa7.grid(row=11, column=2, ipadx=7, ipady=10, padx=5, pady=5)

        mesa8 = tk.Button(fram, text="mesa8", bd=5)
        mesa8.grid(row=11, column=3, ipadx=7, ipady=10, padx=5, pady=5)

        mesa9 = tk.Button(fram, text="mesa9", bd=5)
        mesa9.grid(row=12, column=0, ipadx=7, ipady=10, padx=5, pady=5)

        mesa10 = tk.Button(fram, text="mesa10", bd=5)
        mesa10.grid(row=12, column=1, ipadx=7, ipady=10, padx=5, pady=5)

        mesa11 = tk.Button(fram, text="mesa11", bd=5)
        mesa11.grid(row=12, column=2, ipadx=7, ipady=10, padx=5, pady=5)

        mesa12 = tk.Button(fram, text="mesa12", bd=5)
        mesa12.grid(row=12, column=3, ipadx=7, ipady=10, padx=5, pady=5)


# -------------------ENTRYES------------------------------------
        self.en4 = tk.IntVar()

        E_1 = tk.Entry(self, width=10, bg="white", fg="black")
        E_1.grid(row=1, column=0)

        E_2 = tk.Entry(self, width=50, bg="white", fg="black")
        E_2.grid(row=1, column=1)

        E_3 = tk.Entry(self, width=20, bg="white", fg="black")
        E_3.grid(row=1, column=2)
# ------------------------fila 2-----------------------------
        E_4 = tk.Entry(self, width=10, bg="white",
                       fg="black", textvariable=self.en4)
        E_4.grid(row=2, column=0)
        self.en4.set("$")

        E_5 = tk.Entry(self, width=50, bg="white", fg="black")
        E_5.grid(row=2, column=1)

        E_6 = tk.Entry(self, width=20, bg="white", fg="black")
        E_6.grid(row=2, column=2)
# ------------------------fila 3--------------------------------------
        E_7 = tk.Entry(self, width=10, bg="white", fg="black")
        E_7.grid(row=3, column=0)

        E_8 = tk.Entry(self, width=50, bg="white", fg="black")
        E_8.grid(row=3, column=1)

        E_9 = tk.Entry(self, width=20, bg="white", fg="black")
        E_9.grid(row=3, column=2)

# ---------------------------fila 4---------------------------------
        E_10 = tk.Entry(self, width=10, bg="white", fg="black")
        E_10.grid(row=4, column=0)

        E_11 = tk.Entry(self, width=50, bg="white", fg="black")
        E_11.grid(row=4, column=1)

        E_12 = tk.Entry(self, width=20, bg="white", fg="black")
        E_12.grid(row=4, column=2)


# ---------------------------fila 5--------------------------------
        E_13 = tk.Entry(self, width=10, bg="white", fg="black")
        E_13.grid(row=5, column=0)

        E_14 = tk.Entry(self, width=50, bg="white", fg="black")
        E_14.grid(row=5, column=1)

        E_15 = tk.Entry(self, width=20, bg="white", fg="black")
        E_15.grid(row=5, column=2)

# ----------------------------fila 6------------------------
# -----------------------------fila 7----------------------------
        # ----------------labels-----------------------------------

        la0 = ttk.Label(self, text='Platos y Mesas')
        la0.grid(row=6, column=4)

        la2 = ttk.Label(self, text='Cantidad')
        la2.grid(row=0, column=0)

        la1 = ttk.Label(self, text='Especificacion')
        la1.grid(row=0, column=1)

        la3 = ttk.Label(self, text='Precio')
        la3.grid(row=0, column=2)
