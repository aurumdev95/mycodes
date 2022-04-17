import string
#calculator
def calc(arg):
	sign = ["+", "-", "*", "/"]
	#digits = ["0","1","2","3","4","5","6","7","8","9"]
	letters = string.ascii_letters
	op = False
	all_num = True
	for i in arg:
		for j in sign:
			if i == j:
				op = True
	for e in arg:
		for d in letters:
			if e == d:
				all_num = False
	if op and all_num:
		return eval(arg)
	elif not all_num:
		return "do not include letters, numbers only"
	else:
		return "include operator(+,-,*,/)"
		
def main():
	while True:
		print("calculator..")
		arg = input("input what \n you want to calculate \n -->")
		arg = str(arg)
		print(calc(arg))
		print("done.")
main()
			
	