import pickle


#save init
def save(data, path):
	outputFile = path
	fw = open(outputFile, 'wb')
	pickle.dump(data, fw)
	fw.close()

	
	
	
def load(path):
	inputFile = path
	fd = open(inputFile, 'rb')
	return pickle.load(fd)
	#fd.close()
	
	
def fetch(keyw, path):
	db = load(path)
	for key, value in db["content"].items():
		if key == keyw:
			return value
			
	return "item not found"
	
#db = {"title": "main database", "content": {"car": "tesla"}}
#save(db, "db.data")
#print(load("db.data"))	
#main = {}
	

	
	

	

