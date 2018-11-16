from tkinter import *
import random

root = Tk()
root.geometry("500x500")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

balls = []

for i in range(10):
    x = random.randint(40, 460)
    y = random.randint(40, 460)
    r = 40
    list = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
    dx = random.choice(list)
    dy = random.choice(list)
    oval = canvas.create_oval(x, y, x+r, y+r)
    ball = [x, y, dx, dy, oval]
    balls.append(ball)


def tick_handler():
    global r
    for ball in balls:
        x, y, dx, dy, oval = ball
        if x < 0:
            dx = -dx
            x = 0
        elif x > 500 - r:
            dx = -dx
            x = 500 - r
        if y < 0:
            dy = -dy
            y = 0
        elif y > 500 - r:
            dy = -dy
            y = 500 - r
        x = x + dx
        y = y + dy
        canvas.move(oval, dx, dy)
        ball[0] = x
        ball[1] = y
        ball[2] = dx
        ball[3] = dy


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

speed_scale.set(1)
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
