import string
import json
letters = string.ascii_letters
print(letters)
print(len(letters))
a = letters[26:]
h = []
for i in a:
	#print(type(i))
	h.append(i)
	#print(h)
	
data = {
"upper_letters": ""
}
data["upper_letters"] = h
print(data)
with open('upper_letters.txt', 'w') as f:
	json.dump(data, f)
print("done...")
	


#print(letters.split())
#letter.isupper()