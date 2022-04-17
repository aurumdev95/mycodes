
def reverser(n):
	rev=0
	while(n>0):
	   dig=n%10
	   rev=rev*10+dig
	   n=n//10
	print("Reverse of the number:",rev)
	print("enter 0 to exit")
	
while True:
		n=int(input("Enter number: "))
		if n == 0:
			break
		reverser(n)

