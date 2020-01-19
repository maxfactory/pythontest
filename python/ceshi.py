import turtle
i = 2
colors = ['red','orange','yellow','green','blue','indigo','purple','pink']
a = len(colors)
turtle.hideturtle()
turtle.pensize(10)
turtle.right(30)
while i > 0:
	for x in range(a):
		c = colors[x]
		turtle.color(c)
		turtle.circle(30,240)
		turtle.fd(104)
		turtle.circle(-30,240)
		turtle.fd(104)
		i -= 1
turtle.done()

# import turtle
# turtle.right(30)
# turtle.circle(30,240)
# turtle.done()