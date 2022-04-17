# Python Program to Convert seconds
# into hours, minutes and seconds
  
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
print("《seconds to time program》")
while True:
	n = input(">>input the number of seconds \n you want to convert \n enter 0 to exit:")
	try:
		n = int(n)
	except:
		print(">>this is not a number, pls try again ")
		continue
	if n == 0:
		break
	print(f">>this {n} seconds are equivalent to \n this time:{convert(n)}")
	