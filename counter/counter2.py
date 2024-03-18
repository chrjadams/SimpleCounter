from tkinter import *
from tkinter import ttk
from tkinter import font
from playsound import playsound

count = 0
root = Tk()
bg = "#5ccad6"

s = ttk.Style()
s.configure('test.TFrame', background = bg)
s3 = ttk.Style()
s3.configure('test3.TFrame')

s2= ttk.Style()
s2.configure('test2.TLabel', background = bg, foreground = "#ffffff")

def updateCount():
    #playsound('sounds/1.wav', False)
    global count
    global bg
    bgHere = bg[1:]
    bgToHex = int(bgHere, 16)
    bgToHex = bgToHex + 8
    hexToBg = hex(bgToHex)
    bg = "#" + str(hexToBg)[2:]
    print(bg)
    count = count +1
    label.config(text = count)
    s.configure('test.TFrame', background = bg)
    s2.configure('test2.TLabel', background = bg)

frameA = ttk.Frame(root, style='test.TFrame')
frameA.pack()
frameB = ttk.Frame(frameA, width=300, height = 300, style='test.TFrame')
frameB.pack()
frameC = ttk.Frame(frameB, width=200, height = 200, style='test.TFrame')
frameC.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label = ttk.Label(frameC, text = count)
label.place(relx = 0.5, rely = 0.45, anchor = CENTER)
label.configure(style='test2.TLabel', font = ('Helvetica', 50))

button = ttk.Button(frameC, text="", command=updateCount,  takefocus=False, cursor='arrow')
button.place(relx = 0.5, rely = .75, anchor = CENTER)


root.mainloop()