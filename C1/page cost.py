def priceFind(pgs, mode):
	price = 50 #per page
	if mode == 2:
		if pgs % 2 == 0:
			pg = pgs / 2
		else:
			pgs += 1
			pg = pgs / 2
	elif mode == 4:
		if pgs % 2 == 0:
			pg = pgs / 4
		else:
			pgs += 1
			pg = pgs / 4
		
	else:
		pg = pgs
	return pg * price 
		
while True:
	arg = int(input('enter num of pages:'))
	m = int(input('1 4 or 2:'))
	try:
		print(priceFind(arg, m))
	except:
		print('error')
