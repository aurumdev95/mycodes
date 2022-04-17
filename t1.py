import turtle as t

s = t.Turtle()

def circle():
	for i in range(180):
		s.forward(1)
		s.right(1)
		
for e in range(2):
	s.forward(100)
	circle()
	s.forward(100)
	
s.left(90)

		
for e in range(2):
	s.forward(100)
	circle()
	s.forward(100)

		
s.right(45)
		
for e in range(2):
	s.forward(100)
	circle()
	s.forward(100)
	
s.left(270)

for o in range(5):
		circle()
		s.left(95)
		
t.done()