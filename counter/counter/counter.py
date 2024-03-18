from tkinter import *
from tkinter import ttk

count = 0
root = Tk()


def updateCount():
    global count
    count = count +1
    label.config(text = count)

root.geometry("300x300")

frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text=count, font = ('verdana', 100,))
label.grid(column=0, row=0)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
ttk.Button(frm, text="", command=updateCount).grid(column=2, row=10)
print(label)


root.mainloop()


