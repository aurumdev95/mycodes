
#store data:

import pickle
dataset = ['hello','test']
outputFile = 'test.data'
fw = open(outputFile, 'wb')
pickle.dump(dataset, fw)
fw.close()
#load data:

import pickle
inputFile = 'test.data'
fd = open(inputFile, 'rb')
dataset = pickle.load(fd)
print dataset