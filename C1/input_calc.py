
#problem solver

def area_rect():
	l = input("input the length:")
	w = input("input the width:")
	l = int(l)
	w = int(w)
	print(l * w)

def area_square():
	s = input("input the length of the side:")
	s = int(s)
	print(s * s)
while True:
	num = input("which operation do you want?:").upper()
	if num == "AREA_RECTANGLE":
		area_rect()
	if num == "AREA_SQUARE":
		area_square()
	print("operation success.. ")
	
		
		
	
