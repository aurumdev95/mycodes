from tkinter import *
from converter import *

root = Tk()

font = ('helvetica', 7, 'bold')
def main():
	ans = converter(e.get())
	label.config(text=ans)

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter number')

label = Label(root, text='result', font=font)
label.pack(pady=20)

button = Button(root, text='convert', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="               numbers to words converter ")
root.config(menu=menubar)
root.mainloop()