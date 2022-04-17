from tkinter import *
font = ('helvetica', 7, 'bold')
def main():
    try:
    	menu = int(g.get())
    	if menu < 1 or menu > 2:
    		raise ValueError
    	if menu == 1:
    	   dec = int(e.get())
    	   label.config(text="Binary: {}".format(bin(dec)[2:]))
    	elif menu == 2:
    	   binary = e.get()
    	   label.config(text="Decimal: {}".format(int(binary, 2)))
    except ValueError:
    	label.config(text='error')

root = Tk()


#def click():
#	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter number')

g = Entry(root)
g.pack(pady=20)
g.insert(0, 'choose (1) for dec bin (2) for bin dec')

label = Label(root, text='answer', font=font)
label.pack(pady=20)

button = Button(root, text='convert', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="               binary decimal converter ")
root.config(menu=menubar)
root.mainloop()