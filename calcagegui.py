# -*- coding: utf-8 -*-
import time
from calendar import isleap
from tkinter import *
font = ('helvetica', 7, 'bold')
# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28



def main():
	name = e.get()
	age = f.get()
	localtime = time.localtime(time.time())
	year = int(age)
	month = year * 12 + localtime.tm_mon
	day = 0
	begin_year = int(localtime.tm_year) - year
	end_year = begin_year + year
	# calculate the days
	for y in range(begin_year, end_year):
	       if (judge_leap_year(y)):
	       	day = day + 366
	       else:
	       		day = day + 365
	       		leap_year = judge_leap_year(localtime.tm_year)
	for m in range(1, localtime.tm_mon):
		day = day + month_days(m, leap_year)
		day = day + localtime.tm_mday
	label.config(text=f'{name} age:{age}\nis equivalent to:{month}months and\n{day}days')
	#"%d months or %d days" % (month, day))


root = Tk()


#def click():
#	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter your name')

f = Entry(root)
f.pack(pady=20)
f.insert(0, 'enter your age')

label = Label(root, text='result', font=font)
label.pack(pady=20)

button = Button(root, text='compute', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="               calcutate from age ")
root.config(menu=menubar)
root.mainloop()
