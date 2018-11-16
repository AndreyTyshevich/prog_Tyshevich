import turtle
length = 50
dy = 18
x = 0
y = 0
sides = 3
angle = 360/sides
turtle.shape('turtle')
for number in range(7):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for k in range(sides):
            turtle.left(360-angle)
            turtle.forward(length)
    sides += 1
    angle = 360/sides
    y += dy
    x += 10
    length += 20
    dy += 7
