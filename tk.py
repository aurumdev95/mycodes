from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("image viewer")

var = StringVar()
var.set("hello")
drop = OptionMenu(root, var, "hello", "hello2")
drop.pack()

#my_menu = Menu(root)
#root.config(menu=my_menu)

#def hide():
#	frame.pack_forget()
#	frame2.pack_forget()
#def our_command():
#	pass
#	
#def file_new():
#	hide()
#	frame.pack(fill="both", expand=1)
#	l = Label(frame, text="hello").pack()
#	
#def my_new():
#	hide()
#	frame2.pack(fill="both", expand=1)
#	l2 = Label(frame2, text="hello2").pack()


#	
#			
#file = Menu(my_menu)
#my_menu.add_cascade(label="file", menu=file)
#file.add_command(label="new", command=file_new)
#file.add_separator()
#file.add_command(label="my", command=my_new)
#file.add_separator()
#file.add_command(label="exit", command=root.quit)

#frame = Frame(root, width=300, height=300, bg="red")

#frame2 =Frame(root, width=300, height=300, bg="blue")




#frames
#frame = LabelFrame(root, text="this is a frame", padx=50, pady=50)
#frame.pack()
#b = Button(frame, text="hello")
#b.grid(row=2, column=1)

#frame2 = LabelFrame(root, text="hello2", padx=5, pady=5).pack()
#b2 = Button(frame2, text="hello2")
#b2.pack()


#checkbuttton
#var = StringVar()
#c = Checkbutton(root, text="check tis box", variable=var, onvalue="on", offvalue="off")
#c.deselect()
#c.pack()

#def show():
#	label = Label(root, text=var.get()).pack()


#b = Button(root, text="show", command=show).pack()

root.mainloop()