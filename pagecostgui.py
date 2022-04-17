from tkinter import *
def priceFind(pgs, mode):
	price = 50 #per page
	price2 = 100
	if mode == 2:
		if pgs % 2 == 0:
			pg = pgs / 2
			return pg * price2
		else:
			pgs -= 1
			pg = pgs / 2
			return (pg * price2) + 50
			
	elif mode == 4:
		if pgs % 2 == 0:
			pg = pgs / 4
			return pg * price2
		else:
			if (pgs + 1) % 2 == 0:
				pgs += 1
				pg = pgs / 4
				return (pg * price2) - 50
			else:
				pgs -= 1
				pg = pgs / 4
				return (pg * price2) + 50
				
		
	else:
		pg = pgs
		return pg * price 
		
#while True:
#	arg = int(input('enter num of pages:'))
#	m = int(input('1 4 or 2:'))
#	try:
#		print(priceFind(arg, m))
#	except:
#		print('error')


root = Tk()
def main():
	try:
		price = priceFind(int(e.get()), int(a.get()))
		label.config(text=f'price is:{price}rfw')
	except:
		label.config(text='error')
		

#def click():
#	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter number of pages')

a = Entry(root)
a.pack(pady=20)
a.insert(1, 'enter the layout:1,2 and 4')

label = Label(root, text='cost')
label.pack(pady=20)

button = Button(root, text='get price', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="                  page cost calculator ")
root.config(menu=menubar)
root.mainloop()