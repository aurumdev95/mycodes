#full func sec to time cnv
from tkinter import *

def time(sec):
	yr = 0
	mnth = 0
	day = 0
	hr = 0
	min = 0
	try:
		sec = int(sec)
	except:
		return 'invalid'
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
	return f"yr:{int(yr)} month:{int(mnth)} day:{int(day)} hr:{int(hr)} min:{int(min)} sec:{int(sec)}"
#while True:
#	yr = 0
#	mnth = 0
#	day = 0
#	hr = 0
#	min = 0
#	sec = input("input sec:")
#	try:
#		sec = int(sec)
#	except:
#		print("invalid")
#	if sec >= 60:
#		min = sec / 60
#		sec %= 60
#		#print(int(min))
#	if min >= 60:
#		hr = min / 60
#		min %= 60
#	if hr >= 24:
#		day = hr / 24
#		hr %= 24
#	if day >= 30:
#		mnth = day / 30
#		day %= 30
#	if mnth >= 360:
#		yr = mnth / 360
#		mnth %= 360
	
	

root = Tk()
def main():
	tim = time(int(e.get()))
	label.config(text=tim)

#def click():
#	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter seconds')

label = Label(root, text='time')
label.pack(pady=20)

button = Button(root, text='compute', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="                second to time converter                    ")
root.config(menu=menubar)

root.mainloop()	