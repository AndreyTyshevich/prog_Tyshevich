import graphics as gr
import time

window = gr.GraphWin("pic", 1500, 900)


def draw_picture():
    draw_background()
    draw_sun()
    draw_sun_lines()
    draw_sun_face()
    draw_creature()
    
def draw_background():
    sky= gr.Rectangle(gr.Point(0,0), gr.Point(1500, 450))
    sky.setFill('cyan')

    grass=gr.Rectangle(gr.Point(0,450), gr.Point(1500, 900))
    grass.setFill('green')

    sky.draw(window)
    grass.draw(window)
    
def draw_sun():
    sun = gr.Circle(gr.Point(180, 200), 100)
    sun.setFill('yellow')
    sun.draw(window)
    
def draw_sun_face():
    sun_eye1 = gr.Circle(gr.Point(150, 180), 20)
    sun_eye2 = gr.Circle(gr.Point(250, 180), 15)
    
    sun_eye1_center = gr.Circle(gr.Point(150, 180), 8)
    sun_eye2_center = gr.Circle(gr.Point(250, 180), 7)
    
    sun_eye1.setFill('red')
    sun_eye2.setFill('red')
    
    sun_eye1_center.setFill('black')
    sun_eye2_center.setFill('black')

    sun_eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
    sun_eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
    
    sun_eyebrow1.setWidth(10)
    sun_eyebrow2.setWidth(10)
    
    sun_eyebrow1.setOutline('black')
    sun_eyebrow2.setOutline('black')

    sun_mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
    sun_mouth.setWidth(20)
    sun_mouth.setOutline('black')

    sun_eye1.draw(window)
    sun_eye2.draw(window)
    sun_eye1_center.draw(window)
    sun_eye2_center.draw(window)
    sun_eyebrow1.draw(window)
    sun_eyebrow2.draw(window)
    sun_mouth.draw(window)
    
def draw_sun_lines():
    draw_sun_line (300,300)
    draw_sun_line (400,150)
    draw_sun_line (350,280)
    draw_sun_line (480,120)
    draw_sun_line (250,400)
    draw_sun_line (210,450)
    draw_sun_line (150,500)
    
def draw_sun_line(x, y):
    sunline = gr.Line(gr.Point(150, 180), gr.Point(x, y))
    sunline.setFill('yellow')
    sunline.draw(window)

def destroy_sun_lines():
    anti_sun_line (300,300)
    anti_sun_line (400,150)
    anti_sun_line (350,280)
    anti_sun_line (480,120)
    anti_sun_line (250,400)
    anti_sun_line (210,450)
    anti_sun_line (150,500)
    
def anti_sun_line(x, y):
    antiline = gr.Line(gr.Point(150, 180), gr.Point(x, y))
    antiline.setFill('cyan')
    antiline.draw(window)    
        
def draw_creature():
    face2 = gr.Circle(gr.Point(700, 500), 100)
    face2.setFill('pink')

    eye3 = gr.Circle(gr.Point(650, 480), 20)
    eye4 = gr.Circle(gr.Point(710, 480), 20)
    eye3_center = gr.Circle(gr.Point(650, 480), 8)
    eye4_center = gr.Circle(gr.Point(710, 480), 7)
    eye3.setFill('white')
    eye4.setFill('white')
    eye3_center.setFill('black')
    eye4_center.setFill('black')

    mouth2 = gr.Line(gr.Point(700, 550), gr.Point(710, 580))
    mouth2.setWidth(20)
    mouth2.setOutline('white')

    leg1 = gr.Line(gr.Point(650, 620), gr.Point(680, 550))
    leg1.setWidth(20)
    leg1.setOutline('pink')

    leg2 = gr.Line(gr.Point(750, 620), gr.Point(720, 550))
    leg2.setWidth(20)
    leg2.setOutline('pink')

    face2.draw(window)
    eye3.draw(window)
    eye4.draw(window)
    eye3_center.draw(window)
    eye4_center.draw(window)
    mouth2.draw(window)

    leg1.draw(window)
    leg2.draw(window)

cloud1 = gr.Circle(gr.Point(600, 200), 40)
cloud1.setFill('white')

cloud2 = gr.Circle(gr.Point(650, 200), 40)
cloud2.setFill('white')

cloud3 = gr.Circle(gr.Point(700, 200), 40)
cloud3.setFill('white')

cloud4 = gr.Circle(gr.Point(625, 150), 40)
cloud4.setFill('white')


cloud5 = gr.Circle(gr.Point(675, 150), 40)
cloud5.setFill('white')


draw_picture()
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)

while True==True:
    for i in range (1000):
        time.sleep(0.0001)
        destroy_sun_lines()
        draw_sun()
        draw_sun_lines()
        draw_sun_face()
        cloud1.move(1.5,0)
        cloud2.move(1.5,0)
        cloud3.move(1.5,0)
        cloud4.move(1.5,0)
        cloud5.move(1.5,0)
    for i in range (1000):
        time.sleep(0.0001)
        destroy_sun_lines()
        draw_sun()
        draw_sun_lines()
        draw_sun_face()
        cloud1.move(-1.5,0)
        cloud2.move(-1.5,0)
        cloud3.move(-1.5,0)
        cloud4.move(-1.5,0)
        cloud5.move(-1.5,0)

window.getMouse()

window.close()

    
