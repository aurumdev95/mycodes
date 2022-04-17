import math as m
import random



def expand():
    a = [0]
    while len(a) <= 100:
        a.append(m.ceil(random.random() * 10))
        print(a)
        r = 0
        even = []
    for i in a:
        r = m.sqrt(i)
        r = m.pow(r, 2)
        
        r = m.ceil(r)
        if r % 2 == 0:
            print ("even yeah")
            even.append(r)
        print(r)
    pr = []
    for eve in even:
        pr.append(str(eve)
    #pls ignore compiler
    #print("|".join(pr))
#print("run...")
#expand()
#print("done.")