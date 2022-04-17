#name passwordizer
import string
from random import *

#print(numbers)

def name_rand(n):
	sym = string.punctuation
	symbol = []
	for i in sym:
		symbol.append(i)
	numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	namli = []
	for i in n:
		namli.append(i)
	shuffle(namli)
	for i in range(randrange(2, 5)):
		namli.append(str(choice(numbers)))
		namli.append(choice(symbol))
	name = "".join(namli)
	return name
	
while True:
	n = input("input the name \n u want to passwordize:").lower()
	print(name_rand(n))
	print("done..")	