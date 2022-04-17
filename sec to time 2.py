#full func sec to time cnv
while True:
	yr = 0
	mnth = 0
	day = 0
	hr = 0
	min = 0
	sec = input("input sec:")
	try:
		sec = int(sec)
	except:
		print("invalid")
	if sec >= 60:
		min = sec / 60
		sec %= 60
		#print(int(min))
	if min >= 60:
		hr = min / 60
		min %= 60
	if hr >= 24:
		day = hr / 24
		hr %= 24
	if day >= 30:
		mnth = day / 30
		day %= 30
	if mnth >= 360:
		yr = mnth / 360
		mnth %= 360
	print(f"yr:{int(yr)} month:{int(mnth)} day:{int(day)} hr:{int(hr)} min:{int(min)} sec:{int(sec)}")
	
	