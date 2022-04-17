import pickle
import time
from random import *
from tkinter import *



class Student:
	def __init__(self, name):
		self.name = name
		self.book_borrow = []
		self.donbooks = 0
		
	

class Book:
	def __init__(self, title):
		self.title = title
		self.current_owner = "library"
	def changeOwner(self, userActive):
		self.current_owner = userActive


def libraryCatalog(library):
	size = len(library["books"])
	for i in range(size):
		print('->', library["books"][i].title)

def varName():
	letters = [1, 2, 3, 4, 5]
	x = []
	for i in range(5):
		x.append(str(choice(letters)))
	return "".join(x)
	
	
#libraryCatalog(library)
#creating new student user


nameFile = 'usersave.data'
#import time



#creating new user

#loading saves
def account():
	global library
	global userActive
	try:
		fd = open(nameFile, 'rb')
		library = pickle.load(fd)
		#users = pickle.load(fd)
		fd.close()
		print("load done")
	except:
		b1 = Book("introduction to chemistry")
		b2 = Book("python for beginners")
		b3 = Book("advanced algebra")
		b4 = Book("intro to web dev")
		b5 = Book("biology 8th edition")
		library = {"name": "grand library", "books": [b1, b2, b3, b4, b5], "users": []}
		fw = open(nameFile, 'wb')
		pickle.dump(library, fw)
		fw.close()
	

	
	
account()
	

	
root = Tk()
my_menu = Menu(root)
root.config(menu=my_menu)

font = ('helvetica', 7, 'bold')
	
def login_func():
	hide()
	login.pack()
	title.pack()
	e.pack()
	log_btn.pack()
	sign_btn.pack()
def signin_func():
	hide()
	signin.pack()
	title2.pack()
	a.pack()
	signin_btn.pack()
def login():
	global userActive
	username = e.get()
	for user in library["users"]:
		 			if user.name == username:
		 				userActive = username
def signin():
	#create new user
	global userActive
	siz = len(library["users"])
	name = a.get()
	exec("user{} = Student(name)".format(siz))
	#print(name)
	exec(f'library["users"].append(user{siz})')
	fw = open(nameFile, 'wb')
	pickle.dump(library, fw)
	fw.close()
	userActive = name
		
def view_func():
	hide()
	view.pack()
	title3.pack()
	view()
	iss_btn.pack()
	ret_btn.pack()
	
def view():
	size = len(library["books"])
	for i in range(size):
		cata1 = Label(view, text=f'{ library["books"][i].title}').pack()
		cata2 = Label(view, text=f"current ownership:{library['books'][i].current_owner}").pack()
	           		
	           		
#def issue():
def issue():
	bk = b.get()
	try:
		for book in library["books"]:
			if book.current_owner == "library":
				if book.title == bk:
					book.current_owner = userActive
					for user in library["users"]:
						if user.name == userActive:
							user.book_borrow.append(bk)
							issl.config(text=f'book {bk} has been issued to {userActive}')
	except:
		ssl.config(text="wrong book name")
#issue books
def issue_func():
	hide()
	issuefr.pack()
	title3.pack()
	b.pack
	issl.pack()
	issue_btn.pack()
def return_func():
	hide()
	returnfr.pack()
	title5.pack()
	c.pack()
	ret.pack()
	retr_btn.pack()
def donate():
	s = d.get()
	nm = varName()
	exec(f'b{nm} = Book(s)')
	exec(f'library["books"].append(b{nm})')
	for user in library["users"]:
		if user.name == userActive:
			user.donbooks += 1
			don.config(text=f'{userActive} have donated book \n{s} to mylibrary\nthank you for your kind act.')	
def userr():
	u1 = Label(userfr, text="book(s) in possesion:").pack()
	for user in library["users"]:
		if user.name == userActive:
			for b in user.book_borrow:
				u2 = Label(userfr,text=f'-{b}').pack()
				u3 = Label(userfr, text=f"book(s) donated:{user.donbooks}")
	            
	            
def returnn():
	g = c.get()
	try:
		for user in library["users"]:
			if user.name == userActive:
				for b in user.book_borrow:
					if b == g:
						for bkl in library["books"]:
							if bkl.title == g:
								bkl.current_owner = "library"
								user.book_borrow.remove(g) 
								ret.config(text=f"the book{g} has been returned\nby{ userActive}")

def donate_func():
	hide()
	donatefr.pack()
	title7.pack()
	d.pack()
	don.pack()
	d_btn.pack()
	
def user_func():
	hide()
	userfr.pack()		              	title6.pack()
	userr()
	don_btn.pack()
def exiit():
	fw = open(nameFile, 'wb')
	pickle.dump(library, fw)
	fw.close()
	root.quit()
	
def hide():
	login.pack_forget()
	signin.pack_forget()
	view.pack_forget()
	issuefr.pack_forget()
	returnfr.pack_forget()
  userfr.pack_forget()
	donatefr.pack_forget()
#menus
catalog = Menu(my_menu)
my_menu.add_cascade(label='catalog', menu=catalog)
catalog.add_command(label="all books", command=view_func)
catalog.add_separator()
catalog.add_command(label='')
exit = Menu(my_menu)
my_menu.add_cascade(label='account', menu=exit)
exit.add_command(label="user", command=user_func)
exit.add_separator()
exit.add_command(label='exit', command=exiit)
#frames
#login
login = Frame(root, width=100, height=400)
title = Label(login, text='login')
e.Entry(login)
e.insert(0, 'enter usernname')
#e.pack()
log_btn = Button(login, text='login', command=login)
sign_btn = Button(login, text='sign up', command=signin_func)
#sign up
signin = Frame(root, width=100, height=400)
title2 = Label(signin, text='sign up')
a.Entry(signin)
a.insert(0, 'enter usernname')
#e.pack()
signin_btn = Button(signin, text='sign up', command=signin)
#view
view = Frame(root)
title3 = Label(view, text='welcome to my library\nhere are all books')
iss_btn = Button(view, text='issue books', command=issue_func)
ret_btn = Button(view, text='return book', command=return_func)
#cata = Label(view)
#issue
issuefr = Frame(root)
title4 = Label(issuefr, text='issue a book')
b = Entry(issuefr)
b.insert(0, 'enter book name')
issue_btn =Button(issuefr, text='issue', command=issue_func)
issl = Label(issuefr, text='issue order')
#return
returnfr = Frame(root)
title5 = Label(returnfr, text='return books')
c = Entry(returnfr)
c.insert(0, 'enter book name')
ret = Label(returnfr, text='return order')
retu_btn =Button(returnfr, text='return book', command=returnn)
#user
userfr = Frame(root)
title6 = Label(userfr, text=f'account:{userActive}')
don_btn = Button(userfr, text='donate a book', command=donate_func)
#donate
		  
donatefr = Frame(root)
title7 = Label(donatefr, text='donate a book please')
d = Entry(donatefr)
d.insert(0, 'enter book name')
don = Label(donatefr, text='donate order')
d_btn = Button(donatefr, text='donate', command=donate)
login_func()
root.mainloop()
	
			
#jjajja	
		 
	


