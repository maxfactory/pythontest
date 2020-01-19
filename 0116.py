import turtle
i = 10
n = 20
s = -10
a = 0
colors = ['red','orange','yellow','green','blue','indigo','purple','pink']
turtle.circle(n)
while a < i:
	for col in range(8):
		c = colors[col]
		turtle.color(c,c)
		turtle.begin_fill()
		turtle.penup()
		turtle.goto(0,s)
		s -= 10
		turtle.pendown()
		n += 10
		turtle.circle(n)
		turtle.end_fill()
	a +=1





# turtle.circle(20)
# turtle.penup()
# turtle.goto(0,-10)
# turtle.pendown()
# turtle.circle(30)
# turtle.penup()
# turtle.goto(0,-20)
# turtle.pendown()
# turtle.circle(40)
# turtle.done()