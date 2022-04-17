from time import strftime
from datetime import datetime as dt
import db


PATH = "save_day.data"

class Task():
	def __init__(self, task):
		self.task = task
		self.done = False
		self.time = None
	def complete(self):
		self.done = True
		self.time = time()
		
		
def time():
	return strftime('%I:%M:%S %p')

#tasks = {}
#cdate = dt.strftime(dt.now(), "%m/%d/%Y")
#ctime = dt.strftime(dt.now(), "%H/%M/%S")

#print(cdate, ctime)


	
#print(task)
	
	
#ddb = db.load(PATH)
#ddb["content"].append(Task("test"))
#db.save(ddb, PATH)
#print(ddb)

#main loop
print("welcome")
ddb = db.load(PATH)
while True:
	for c in ddb["content"]:
		print(c.task, c.done, c.time)
	
	arg = input("input a finished task:").lower()
	try:
		for d in ddb["content"]:
			if arg == d.task:
				d.complete()
		db.save(ddb["content"], PATH)
	except Exception as e:
		print(e, "error in typing")
	
	
	

