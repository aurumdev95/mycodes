from tkinter import *

root = Tk()
my_menu = Menu(root)
root.config(menu=my_menu)

font = ('helvetica', 7, 'bold')
def click():
	pass
	
def file_new():
	hide()
	frame.pack(fill='both')
	label.pack()
def another():
	hide()
	frame2.pack(fill='both')
	label2.pack()
def hide():
	frame.pack_forget()
	frame2.pack_forget()
	

#e = Entry(root)
#e.pack(pady=20)
#e.insert(0, 'enter your name')


#label.pack(pady=20)


#frame = LabelFrame(root, text="hello world", padx=5, pady=10).pack(pady=50, padx=10)

#button = Button(frame, text='button')
#button.pack()

#button2 = Button(frame, text='button2')
#button2.pack()
#clicked = StringVar()
#clicked.set('hi')
#menu = OptionMenu(root, clicked, 'hello', 'world')
#menu.pack(pady=100)

#menubar = Menu(root)
#menubar.add_cascade(label="               test ")
#root.config(menu=menubar)
file_menu = Menu(my_menu)
my_menu.add_cascade(label='file', menu=file_menu)
file_menu.add_command(label="new", command=file_new)
file_menu.add_separator()
file_menu.add_command(label='exit', command=root.quit)

option_menu = Menu(my_menu)
my_menu.add_cascade(label='edit', menu=option_menu)
option_menu.add_command(label="cut", command=another)
option_menu.add_separator()
option_menu.add_command(label='copy', command=click)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='options', menu=edit_menu)
edit_menu.add_command(label="find", command=click)
edit_menu.add_separator()
edit_menu.add_command(label='find next', command=click)
frame = Frame(root, width=50, height=100, bg="yellow")
frame2 = Frame(root, width=50, height=100, bg='red')
label = Label(frame, text='you clicked')
label2 = Label(frame2, text='you clicked')
root.mainloop()