import turtle
length = 50
dy = 18
x = 0
y = 0
t = 3
angle = 360//t
turtle.shape('turtle')
for i in range(7):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for k in range(t):
            turtle.left(360-angle)
            turtle.forward(length)
    t += 1
    angle = 360/t
    y += dy
    x += 10
    length += 20
    dy += 7
