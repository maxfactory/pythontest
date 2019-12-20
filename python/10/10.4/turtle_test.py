import turtle as tl
a = 0
while a < 4:
	tl.forward(200)
	tl.left(90)
	a += 1
# tl.forward(100)
tl.penup()
tl.goto(100,100)
tl.pendown()
tl.circle(100)
tl.done()