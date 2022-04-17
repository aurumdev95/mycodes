from random import *
word = ""
choices = [0, 1]
for i in range(100):
	num = str(choice(choices))
	word = word + num
print(">>> " + word)
binary = str(word)
dec = int(binary, 2)
print("dec:", dec)
	
	
