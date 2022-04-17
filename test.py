#-----brief------#
#next time add a way to keep info in order of title.time.body for ease of access
#add task time comparison with current time to know if it is expired 
#if possible add a way to save tasks

#import json
import time
#with open("tdl_save.json", "w") as f:
#	json.dumps(todo, f)

class Task:
	def __init__(self):
		self.title = ""
		self.time = []
		self.body = ""
	def printTask(self):
		pass
	
def display(todo=""):
		print("your to do list")
		print("________________")
		for i in range(len(todo["content"])):
			print(i+1, ":",  todo["content"][i].title)
			print("//",todo["content"][i].time[0], ".     ", todo["content"][i].time[1])
			print("=>", ":",  todo["content"][i].body)
		#print("      ")
#time sec
lt = time.localtime(time.time())
cyr = lt.tm_year
cmon = lt.tm_mon
cday = lt.tm_mday
chr = lt.tm_hour
cmin = lt.tm_min		
#tim = time.strftime('%I:%M:%S %p')
#print(lt)
todo = {"greetings": "hello", "content": []}
size = len(todo["content"])
print("to do list //ver 0.4.5 test")
while True:
	a = size + 1
	for i in range(1):
	 exec ("obj{} = Task()".format(a)) 
	cnt = []
	txt = ""
	#tm = None
	title = input("input task title:").upper()
	date = input("add date of the task(format(day/month/year)):")
	time = input("add time of task(hr/min)")
	body = input("input task description:").lower()
	yr = None
	mon = None
	dy = None
	hr = None
	min = None
	try:
		title = str(title)
		body = str(body)
		date = str(date)
		time = str(time)
		dy, mon, yr = date.split("/") 
		hr, min = time.split("/")
		dt = dy + "," + mon + "," +  yr
		tm = hr + ":" + min		 
	except:
		print("error")
	exec (f'obj{a}.title = title')
	exec (f"obj{a}.time.append(dt)")
	exec (f"obj{a}.time.append(tm)")
	exec (f'obj{a}.body = body')
	#cnt.append(tm)
	#cnt.append(body)
	#txt = "\n".join(cnt)
	#exec('todo["content"].append(obj{a})')
	exec('todo["content"].append(obj{})'.format(a))
	#print(todo)
	#print(todo["content"])
	display(todo=todo)
	
	
	