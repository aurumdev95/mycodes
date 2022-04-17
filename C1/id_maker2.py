import random

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
    alais = ""
    gender = input("I am (M/F):").upper()
    if gender == "M" or gender == "MALE":
        alias = "man"
    if gender == "F" or gender == "FEMALE":
        alias = "woman"
    print("________intro_________")
    print(f"my name is {name}  \n gender is {gender} \n I am {age}")
    print("".join(ida))
    if age >= 65:
        print(f"hello old{alais}")
    elif age < 65 and age >= 30:
        print(f"hey adult{alais}")
    elif age <= 30 and age >= 18:
        print(f"hi young{alais}")
    else:
        print("yo teen")

var = id_maker()

intro(var)
