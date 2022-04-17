#import androidhelper
import time
import random
from gtts import gTTS
from random import randrange
from playsound import playsound
import os
#imp code
#time
	#time.strftime("%I %M %p on %A, %B %e, %Y")
#taking pictures
#droid.cameraInteractiveCapturePicture('/sdcard/qpython.jpg')





def speakMod(text):
    text = str(text)
    aud = gTTS(text=text, lang="en")
    r = str(randrange(100, 100000))
    path = r + "mp3"
    aud.save(path)
    playsound(path)
    os.remove(path)
    
    
    
    
class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.ai_name = "ai"
        
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age
        
        
def response(text):
    text = str(text)
    if checkExist(["hey", "hello", "hola", "hi"], text):
        greetings = ["hello sir what can I do for you","hello lets get started"]
        ans = random.choice(greetings)
        speakMod(ans)
    if checkExist(["search for","what is","on google"], text):
        print("check..")
        speakMod("check...")
    
    
    
    
    if checkExist(["what time","show time"], text):
	       tim = time.strftime("%I %M %p on %A, %B %e, %Y")
	       print(tim)
	       tim = str(tim)
	       speakMod(tim)
    if checkExist(["get me an id","make id","i need an id","run id maker"], text):
       print("making id")
       ida = id_maker()
       speakMod("here is your  id")
       print("".join(ida))
       print("done..")
    	   



def checkExist(terms, text):
    for i in terms:
        if i in text:
            return True
        
    



def id_maker():
    var = []
    i = 0
    while i <= 15:
        var.append(str(random.randrange(1, 10)))
        i += 1
    return var


person = Person()
while True:
    print("test......")
    
    text = input("enter text you want to speak:").lower()
    text = str(text)
    if text == "exit":
        break
    response(text)
    
    #speakMod(text)   
        

    
