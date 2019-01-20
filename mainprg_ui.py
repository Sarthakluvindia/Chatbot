from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to my Tennis Chatbot")
window.geometry('350x200')
courtsurface = ['home','car','rv']
tournament = ['home','car','rv']
series = ['home','car','rv']

lbl = Label(window, text="Player 1 Name:  ")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)

lbl = Label(window, text="Player 2 Name:  ")

lbl.grid(column=0, row=2)

txt = Entry(window, width=10)

txt.grid(column=1, row=2)

lbl = Label(window, text="Court Surface:  ")

lbl.grid(column=0, row=3)

combo = Combobox(window,width=8,value=courtsurface)

combo.grid(column=1, row=3)

lbl = Label(window, text="Tournament:  ")

lbl.grid(column=0, row=4)

combo = Combobox(window,width=8,value=tournament)

combo.grid(column=1, row=4)

lbl = Label(window, text="Series:  ")

lbl.grid(column=0, row=5)

combo = Combobox(window,width=8,value=series)

combo.grid(column=1, row=5)

window.mainloop()