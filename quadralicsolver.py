#ax2 +- bx +- c = 0
def square(n):
	return n * n
def rng():
	num = []
	for j in range(100):
		num.append(j)
		num.append(-j)
	return num
	
lst = rng()
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print(f"{a}x2 + {b}x + {c} = 0")
x = []
for i in lst:
	#print(i)
	ao = square(i) * a
	bo = b * i
	co = c
	eq = ao + bo + co
	#print(eq)
	if eq == 0:
		x.append(i)
	if len(x) == 2:
		break
print(x)
#print(f"solution:{x[0]},{x[1]}")
		