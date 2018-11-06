import turtle 

turtle.shape('turtle')
turtle.speed('fastest')

vloz = int(input())


def krivo(l, deep):
    if deep == 0:
        turtle.forward(l)
    else:
        krivo(l/3, deep - 1)
        turtle.left(60)
        krivo(l/3, deep - 1)
        turtle.right(120)
        krivo(l/3, deep - 1)
        turtle.left(60)
        krivo(l/3, deep - 1)
        
        
turtle.penup()
turtle.goto(-300, 150)
turtle.pendown()
for y in range(3):
    krivo(600, vloz)
    turtle.right(120)
