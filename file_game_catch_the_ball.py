from tkinter import *
import random
root = Tk()
root.geometry('1400x700')       
canv = Canvas(root, bg="white")
canv.pack(fill=BOTH, expand=1)

col = ['green', 'red', 'blue', 'yellow', 'pink', 'orange']

points = 0
antipoints = 0
minuspoint = 0


def tick():
    global xc, yc, rc, circle, antipoints, minuspoint
    canv.delete(circle)
    canv.delete(ALL)
    xc = random.randint(150, 1250)
    yc = random.randint(150, 550)
    rc = random.randint(20, 140)
    circle = canv.create_oval(xc - rc, yc - rc, xc + rc, yc + rc, fill=random.choice(col))
    canv.create_text(500, 50, text="Счёт:", font='Arial 25')
    canv.create_text(500, 100, text=points, font='Arial 25')
    canv.create_text(900, 50, text="Промахи:", font='Arial 25')
    if minuspoint > 0:
        antipoints += 1
    canv.create_text(900, 100, text=antipoints, font='Arial 25')
    minuspoint = 0
    root.after(800, tick)


def left_button(event):
    global points, minuspoint, xc, yc, rc
    if (event.x-xc)**2 + (event.y-yc)**2 <= rc**2:
        points += 1
        rc = 0
        minuspoint = -100
    else:
        minuspoint += 1


root.bind('<Button-1>', left_button)
circle = canv.create_oval(-100, 0, 0, 0)
tick()
mainloop()
