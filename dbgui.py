from tkinter import *
from tkinter import messagebox
import db

root = Tk()
PATH = "db.data"
root.title("db query program")

my_menu = Menu(root)
root.config(menu=my_menu)


def query():
	t.config(text=str(db.fetch(e.get(), PATH)))

def hide():
	db_q_frame.pack_forget()
	db_n_frame.pack_forget()

def db_n():
	hide()
	db_n_frame.pack()
	title2.grid(column=1, row=1, columnspan=2, pady=10)
	e2.grid(column=1, row=2, padx=5, pady=10)
	e3.grid(column=2, row=2, padx=5, pady=10)
	chl.grid(column=1, row=3, pady=10)
	ch.grid(column=3, row=3, pady=10)
	b2.grid(column=1, row=4)
	b3.grid(column=2, row=4)
	s.grid(column=1, row=6, pady=50, columnspan=2)
	
def db_q():
	hide()
	db_q_frame.pack()
	title1.pack()
	e.pack(pady=10)
	b.pack(pady=20)
	t.pack(pady=20)
	
	

	
def display():
	ddb = db.load(PATH)
	d = []
	for key, value in ddb["content"].items():
		d.append(key+": "+str(value))
	s.config(text="\n".join(d))
	
def add():
	ddb = db.load(PATH)
	if var.get() == "off":
		ddb["content"][e2.get()] = e3.get()
		db.save(ddb, PATH)
		#e3.insert(0,)
		#e2.insert(0,)
		messagebox.showinfo(title="db", message=f"{e2.get()} added to database ")
	else:
		ddb["content"][e2.get()] = e3.get().split(",")
		db.save(ddb, PATH)
		#e3.insert(0,)
		#e2.insert(0,)
		messagebox.showinfo(title="db", message=f"{e2.get()} added to database ")

	
		
db_n_frame = Frame(root, width=400, height=400)

db_q_frame = Frame(root, width=400, height=400)
#db query wigets
			
title1 = Label(db_q_frame, text="databse query program".upper())

e = Entry(db_q_frame)
e.insert(0, "enter query")
#e.pack(pady=20)

b = Button(db_q_frame, text="SEARCH", command=query)
#b.pack(pady=20)

t = Label(db_q_frame, text="info here")
#t.pack(pady=20)

#db new widgets
			
title2 = Label(db_n_frame, text="databse editor program".upper())

e2 = Entry(db_n_frame, width=10)
e2.insert(0, "key")
e3 = Entry(db_n_frame, width=10)
e3.insert(0, "value")
#e.pack(pady=20)
chl = Label(db_n_frame, text="multiple items(,)")

var = StringVar()
ch = Checkbutton(db_n_frame, variable=var, onvalue="on", offvalue="off")
ch.deselect()
#b.pack(ipadx=10, ipady=10)


b2 = Button(db_n_frame, text="ADD", command=add)
b3 = Button(db_n_frame, text="SHOW", command=display)

s = Label(db_n_frame, text="display here")

#b.pack(pady=20)




file = Menu(my_menu)
my_menu.add_cascade(label="db    ", menu=file)
file.add_command(label="new", command=db_n)
file.add_separator()
file.add_command(label="db query", command=db_q)
file.add_separator()
file.add_command(label="exit", command=root.quit)



db_n()


root.mainloop()