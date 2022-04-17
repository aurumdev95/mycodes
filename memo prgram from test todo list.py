#-----brief------#
#yhis one is derived from test.py which was a to do list program
#path = 'save.data'  
path = 'test.data'

#modules
import time
import pickle

#title
print("my memo //ver 0.5.4 alpha")

#memo class
class Memo:
	def __init__(self):
		self.title = ""
		self.time = []
		self.body = ""
	def printMemo(self):
		pass
#displaying function	
def display(memos=""):
		print("your to do list")
		print("________________")
		for i in range(len(memos["content"])):
			print('-------------')
			print(i+1, ":",  memos["content"][i].title)
			print("//",memos["content"][i].time[0], ".     ", memos["content"][i].time[1])
			print("=>", ":",  memos["content"][i].body)
#time 
lt = time.localtime(time.time())
	
#save init
try:
	inputFile = path
	fd = open(inputFile, 'rb')
	memos = pickle.load(fd)
	display(memos=memos)
	
except:
	memos = {"program": "my memo", "content": []}
	outputFile = path
	fw = open(outputFile, 'wb')
	pickle.dump(memos, fw)
	fw.close()
size = len(memos["content"])


#program loop
print("~~~~~~~~~~~~~~~~~~")
while True:
	a = size + 1
	for i in range(1):
	 exec ("obj{} = Memo()".format(a)) 
	cnt = []
	txt = ""
	title = input("input your memo  title:").upper()
	body = input("input your note:").capitalize()
	title = str(title)
	body = str(body)
	cyr = str(lt.tm_year)
	cmon = str(lt.tm_mon)
	cday = str(lt.tm_mday)
	chr = str(lt.tm_hour)
	cmin = str(lt.tm_min)
	csec = str(lt.tm_sec)	
	dt = cday + "," + cmon + "," +  cyr
	tm = chr + ":" + cmin + ":" + csec		 
	exec (f'obj{a}.title = title')
	exec (f"obj{a}.time.append(dt)")
	exec (f"obj{a}.time.append(tm)")
	exec (f'obj{a}.body = body')
	exec('memos["content"].append(obj{})'.format(a))
	display(memos=memos)
	outputFile = path
	fw = open(outputFile, 'wb')
	pickle.dump(memos, fw)
	fw.close()
	
	
	