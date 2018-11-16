import turtle
turtle.shape('turtle')


def square(length):
    for sides in range(4):
        turtle.forward(length)
        turtle.left(90)


l = 20
for number in range(10):
    square(l)
    l += 10
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
