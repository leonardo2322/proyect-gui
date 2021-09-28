from tkinter import *

root = Tk()
frame = Frame(root)
img = PhotoImage(file="descarga.png")
fondo = Label(frame, image=img)
can = Canvas(root)
can.grid()
can.create_image(20, 20, image=img, anchor=NW)

root.mainloop()
"""        fondo = tk.Label(self, image=img)
        fondo.config(bd=12, relief="sunken")
        fondo.grid(row=4, column=1)
        """
