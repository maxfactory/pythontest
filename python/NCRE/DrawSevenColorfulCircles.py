import turtle
colors = ['red','orange','yellow','green','blue','indigo','purple','pink']
a = len(colors)
for i in range(a):
    c = colors[i]
    turtle.color(c,c)
    turtle.begin_fill()
    turtle.rt(360/a)
    turtle.circle(50)
    turtle.end_fill()
turtle.done()
