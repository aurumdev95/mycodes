import turtle

a = turtle.Turtle()

a.speed(5)

for i in range(360):
	a.forward(500)
	a.right(i)
	a.backward(500)
	a.left(360-i)
	
	