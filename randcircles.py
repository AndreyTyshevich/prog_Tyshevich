from tkinter import *
import random
root = Tk()
root.geometry('800x600')        # размер окна 800x600
canv = Canvas(root, bg="white")
canv.pack(fill=BOTH, expand=1)

col = ['green', 'red', 'blue', 'cian', 'yellow', 'pink']

def left_button(event):
    x = event.x
    y = event.y
    r = 50
    canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(col))
    
def right_button(event):
    canv.delete(ALL)
    

root.bind('<Button-1>', left_button)
root.bind('<Button-2>', right_button)

mainloop()
