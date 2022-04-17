# Python Program to Convert seconds
# into hours, minutes and seconds
  
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hour >= 24:
      hour = 0
      day = hour / 24
      return "%d:%d:%02d:%02d" % (day, hour, minutes, seconds)
    else:
      return "%02d:%02d:%02d" % (hour, minutes, seconds)
      
    
      
# Driver program
print("《seconds to time program》")
while True:
	#n = input(">>input the number of seconds \n you want to convert \n enter 0 to exit:")
	n = 123456578499930
	try:
		n = int(n)
	except:
		print(">>this is not a number, pls try again ")
		continue
	if n == 0:
		break
	print(f">>this {n} seconds are equivalent to \n this time:{convert(n)}")
	break
	