import pickles


#a todo list app
class todo():
	def __init__(self, msg, time, done):
		self.message = msg
		self.time = time
		self.done = done
		
	def display_terminal(self):
		print(f"{self.message},{self.time},{self.done}")
		
while True:
	arg = str(input("new item:")).lower()
	if arg 
	