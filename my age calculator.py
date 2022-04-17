#age calculator
import time


def calculateAge(day, month, year):
	age = 0
	lt = time.localtime(time.time())
	current_yr = lt.tm_year
	c_month = lt.tm_mon
	c_day = lt.tm_mday
	#find bd
	isbd = None
	if month < c_month:
		isbd = True
	elif month == c_month:
		if day <= c_day:
			isbd = True
	else:
		isbd = False
	age = current_yr - year
	if not isbd:
		age -= 1
	return age
	
		
		
		

#print(lt)



while True:
	name = input("input your name:").lower()
	name.capitalize()
	day = input("input day of birth(numbers only)(1-30/31):")
	month = input("input month of birth(numbers only)(1-12):")
	year = input("input year of birth:")
	try:
		day = int(day)
		month = int(month)
		year = int(year)
	except:
		print("input numbers on day, month, year")
		continue
	print(name, " age is:", calculateAge(day, month, year))
	