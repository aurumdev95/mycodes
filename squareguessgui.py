#from math import *
#square root approximator
from tkinter import *
font = ('helvetica', 7, 'bold')
def square(n):
	return n * n
def guesser(num):
	guess1 = 0
	guess2 = 1
	while True:
		if square(guess2) == num:
			return guess2
		else:
			if num > guess1 and num < square(guess2):
				return (guess1 + guess2)/2
				break
			else:
				guess1 = guess2
				guess2 += 1

def approxima(guess, num):
		approx = num / guess
		avg = (approx + guess)/2
		for i in range(20):
			if places(avg):
				break
			else:
				approx = num / avg
				avg = (approx + avg) / 2
		return avg

def places(dec):
		dec = str(dec)
		count = 0
		point = False
		for i in dec:
			if point == True:
				count += 1
			elif i == ".":
				point = True
			else:
				continue
		if count >= 3:
			return True
		else:
			return False
#while True:
#	num = int(input("input the square to guess:"))
#	guess = guesser(num)
#	if type(guess) == "int":
#		print(f"the approximate squareroot of {num} is:{guess}")
#		#print(sqrt(num))
#	else:
#		guess = approxima(guess, num)
#		print(f"the approximate squareroot of {num} is:{guess}")
#		#print(sqrt(num))
#		arg = str(input("do you want to continue(y/n):")).lower()
#		if arg == "n":
#			break
#		else:
#			continue


root = Tk()
def main():
	num = int(e.get())
	guess = guesser(num)
	if type(guess) == "int":
		label.config(text='the approximate square root:' + guess)
	#print(f"the approximate squareroot of {num} is:{guess}")
	else:
		guess = approxima(guess, num)
		label.config(text=f'the approximate square root: {guess}')



e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter square')

label = Label(root, text='answer', font=font)
label.pack(pady=20)

button = Button(root, text='compute', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="               approximate square guesser app  ")
root.config(menu=menubar)
root.mainloop()