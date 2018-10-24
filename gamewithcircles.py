from tkinter import *
import random
root = Tk()
root.geometry('1500x800')      
canv = Canvas(root, bg="white")
canv.pack(fill=BOTH, expand=1)

col = ['green', 'red', 'blue', 'yellow', 'pink', 'orange']

def tick():
    root.after(1000, tick)
    canv.delete(ALL)
    x = random.randint(150, 1350)
    y = random.randint(150, 650)
    r = random.randint(20, 140)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(col))

tick()

mainloop()
