import turtle
turtle.shape('turtle')
sides = int(input())
angle = 180 - 360/sides
for y in range(sides):
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(angle) 
