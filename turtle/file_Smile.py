import turtle
a = True
x = 0
turtle.shape('turtle')
turtle.right(300)
turtle.pen(fillcolor="yellow", pencolor="black", pensize=1)
while a:
    turtle.begin_fill()
    for x in range(720):
        turtle.forward(1)
        turtle.left(0.5)
    turtle.end_fill()
    turtle.pen(fillcolor="blue", pencolor="black", pensize=1)
    turtle.penup()
    turtle.goto(-40, 30)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(120):
        turtle.forward(1)
        turtle.left(3)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-80, 30)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(120):
        turtle.forward(1)
        turtle.left(3)
    turtle.end_fill()
    turtle.pen(pensize=5)
    turtle.penup()
    turtle.goto(-50, 30)
    turtle.pendown()
    turtle.forward(1)
    turtle.penup()
    turtle.goto(-90, 30)
    turtle.pendown()
    turtle.forward(1)
    turtle.pen(pensize=1)
    turtle.penup()
    turtle.goto(-90, -90)
    turtle.pendown()
    turtle.pen(fillcolor="blue", pencolor="red", pensize=5)
    for x in range(90):
        turtle.forward(1)
        turtle.left(2)
    while a:
        turtle.penup()
        turtle.forward(100) 
