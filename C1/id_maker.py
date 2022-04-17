import random
import 

def id_maker():
    var = []
    i = 0
    while i <= 15:
        var.append(str(random.randrange(1, 10)))
        i += 1
    return var


    
def intro(ida):
    name = input("my name is:")
    age = input("my age is:")
    age = int(age)
    print(f"my name is {name} \n I am {age}")
    print("".join(ida))
var = id_maker()

intro(var)
