from tkinter import *
from hideinfo import *

root = Tk()

font = ('helvetica', 12, 'bold')
font='Verdana 30 bold'
font=('calibri', 20, 'bold')


title = Label(root, text="you can hide information")
title.pack(pady=20)

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter info you want to hide')

#label = Label(root, text='enter your name')
#label.pack(pady=20)

button = Button(root, text='button')
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="    hide info gui")
root.config(menu=menubar)




root.mainloop()