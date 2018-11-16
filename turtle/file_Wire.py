import turtle
turtle.shape('turtle')


def wire(loop):
    for side in range(180):
        turtle.right(1)
        turtle.forward(loop)
        
        
turtle.penup()
turtle.goto(-350, 0)
turtle.left(90)
turtle.pendown()
for number in range(7):
    wire(1)
    wire(0.25)
