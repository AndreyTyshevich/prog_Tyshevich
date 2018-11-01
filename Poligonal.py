import turtle
turtle.shape('turtle')
l=10
y=2
x=3
def figure(name):
    turtle.penup()
    turtle.goto(y/2,2*y)
    turtle.pendown()
    u=360/name
    turtle.right(u)
    for x in range (name):
        turtle.forward(l)
        turtle.right(u)
    turtle.left(u)
for o in range (10):
    figure(x)
    l+=10
    y+=5
    x+=1


    
