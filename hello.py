from tkinter import *
from tkinter import ttk

root = Tk()
ttk.Button(root, text="Hello World", bg="orange", fg="red").grid()

lbl = Label(root, text="Hello", font=("Arial Bold", 50))
root.geometry('350x200')
lbl.grid(column=0, row=0)

root.mainloop()


