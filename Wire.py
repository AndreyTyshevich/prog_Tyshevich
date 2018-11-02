import turtle
turtle.shape('turtle')
def pruzhina1 (vitok1):
    for x in range (180):
        turtle.right(1)
        turtle.forward(vitok1)
def pruzhina2 (vitok2):
    for x in range (180):
        turtle.right(1)
        turtle.forward(vitok2)
turtle.penup()
turtle.goto(-350,0)
turtle.left(90)
turtle.pendown()
for y in range (7):
    pruzhina1 (1)
    pruzhina2 (0.25)
        
