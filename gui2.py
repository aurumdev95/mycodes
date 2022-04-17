from tkinter import *

root = Tk()

font = ('helvetica', 12, 'bold')
font='Verdana 30 bold'
font=('calibri', 20, 'bold')
def click():
	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter your name')

label = Label(root, text='enter your name')
label.pack(pady=20)

button = Button(root, text='button', command=click)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="               test ")
root.config(menu=menubar)
root.mainloop()