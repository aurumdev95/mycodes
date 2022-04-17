#todo list appp
import pickle
import tkinter as tk
from datetime import datetime
path = 'save.data'
f1 = ("poopins", 15, "bold")
f2 = ("poopins", 13, "bold")
f3 = ("poopins", 10, "normal")

class Todo():
	def __init__(self, message):
		self.message = message
		self.time = datetime.now().strftime("%m:%d:%Y:%H:%M:%S")
		self.done = False
		
memos = []
def load(path=path):
	inputFile = path
	fd = open(inputFile, 'rb')
	memos = pickle.load(fd)
	fd.close()
	return memos

def save(todom, path=path, memos=memos):
	memos.append(Todo(todom))
	outputFile = path
	fw = open(outputFile, 'wb')
	pickle.dump(memos, fw)
	fw.close()
			
def display(memos=memos):
	lab = []
	for i in memos:
		dipla = tk.Label(root, font=f2)
		dipla.config(text=i.message+""+i.time)
		dipla.pack(pady=10)
		lab.append(dipla)
		
	
		
		
def form():
	title2 = tk.Label(root, text="new todo", font=f3).pack(pady=10)
	e = tk.Entry(root) 
	e.pack(pady=10)
	b = tk.Button(root, text="new", command=click).pack(pady=10)
		

def click():
	save(e.get())
	display()
				

root = tk.Tk()

title = tk.Label(root, text="todo app", font=f1)
title.pack()

form()

menubar = tk.Menu(root)
menubar.add_cascade(label="todo list app")
root.config(menu=menubar)


root.mainloop()