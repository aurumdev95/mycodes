#import androidhelper
import time
import random
#imp code
#time
	#time.strftime("%I %M %p on %A, %B %e, %Y")
#taking pictures
#droid.cameraInteractiveCapturePicture('/sdcard/qpython.jpg')



droid = androidhelper.Android()

def speakMod(text):
    text = str(text)
    text.lower()
    print(f"{person.ai_name}: {text}..")
    droid.ttsSpeak(text)
    
    
    
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
    
    if checkExist(["open camera","take a picture"], text):
        speakMod("opening camera.....")
        n = str(random.randrange(100, 1000000))
        name =  "cam" + n + "jpg"
        droid.cameraInteractiveCapturePicture(name)
    
    
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
        

    
