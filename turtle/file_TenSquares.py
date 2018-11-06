import turtle
turtle.shape('turtle')


def kv(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)


k = 20
for x in range(10):
    kv(k)
    k += 10
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
