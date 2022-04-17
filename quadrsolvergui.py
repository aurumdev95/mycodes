from math import sqrt
from tkinter import *
#quadratic equation solver
def square(n):
	return n * n
def quadrsolv(a, b, c):
	ao = square(b) - (4 * a * c)
	try:
		ao = sqrt(ao)
	except:
		return "math error"
	xpos = (-b + ao)/(2 * a)
	xneg = (-b - ao)/(2 * a)
	x = [xpos, xneg]
	return x
#ans = []
#while True:
#	#testing module
#	a = int(input("a:"))
#	b = int(input("b:"))
#	c = int(input("c:"))
#	sol = quadrsolv(a, b, c)
#	ans.append(sol)
#	print("the solution:",sol)
#	print('all answers', ans)


root = Tk()

def main():
	av = int(a.get())
	bv = int(b.get())
	cv = int(c.get())
	sol = quadrsolv(av, bv, cv)
	label.config(text=f'solutin set: {sol}')
	
#def click():
#	label.config(text='hello:' + e.get())

title = Label(root, text='format: ax^2+bx+c=0')
title.pack(pady=20)

a = Entry(root)
a.pack(pady=20)
a.insert(0, 'enter a')

b = Entry(root)
b.pack(pady=20)
b.insert(0, 'enter b')

c = Entry(root)
c.pack(pady=20)
c.insert(0, 'enter c')

label = Label(root, text='answer')
label.pack(pady=20)

button = Button(root, text='compute', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="                     quadratic equation solver")
root.config(menu=menubar)

root.mainloop()