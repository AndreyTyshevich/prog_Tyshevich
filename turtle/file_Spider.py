import turtle
turtle.shape('turtle')
x = int(input())
u = 180 - 360/x
for y in range(x):
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(u) 
