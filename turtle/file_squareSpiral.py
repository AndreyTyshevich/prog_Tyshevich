import turtle
turtle.shape('turtle')
length = 10
for side in range(100):
    turtle.forward(length)
    turtle.left(90)
    length += 5
