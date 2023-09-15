from tkinter import *
from time import *

w = Tk()
w.title("Digital clock")
w.geometry("620x170")
w.resizable(1,1)

label = Label(w,
    font=("Arial", 74, "bold"),
    bg="red",
          fg="blue",
          bd=25)

label.grid(row=0, column=1)

def update():
    t = strftime("%I:%M:%S %p")
    label.config(text=t)
    w.after(1000, update)

update()
w.mainloop()