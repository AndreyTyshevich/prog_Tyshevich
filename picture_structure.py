import graphics as gr


window = gr.GraphWin("pic", 1500, 900)

def draw_sun():
    sun = gr.Circle(gr.Point(180, 200), 100)
    sun.setFill('yellow')
    sun.draw(window)

    
def draw_sun_lines():
    draw_sunline(450, 180)

    draw_sunline(420, 200)

    draw_sunline(390, 280)

    draw_sunline(370, 250)

    draw_sunline(350, 230)

    draw_sunline(330, 200)

    draw_sunline(300, 290)

    draw_sunline(290, 250)

    draw_sunline(250, 280)

    draw_sunline(230, 350)

    draw_sunline(200, 370)

    draw_sunline(100, 450)
    
def draw_sunline(x,y):
    sunline = gr.Line(gr.Point(150, 180), gr.Point(x, y))
    sunline.setFill('yellow')

    sunline.draw(window)
    
def draw_sun_face():
    eye1 = gr.Circle(gr.Point(150, 180), 20)
    eye2 = gr.Circle(gr.Point(250, 180), 15)
    
    eye1_center = gr.Circle(gr.Point(150, 180), 8)
    eye2_center = gr.Circle(gr.Point(250, 180), 7)
    
    eye1.setFill('red')
    eye2.setFill('red')
    
    eye1_center.setFill('black')
    eye2_center.setFill('black')

    eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
    eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
    
    eyebrow1.setWidth(10)
    eyebrow2.setWidth(10)
    
    eyebrow1.setOutline('black')
    eyebrow2.setOutline('black')

    mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
    mouth.setWidth(20)
    mouth.setOutline('black')

    eye1.draw(window)
    eye2.draw(window)
    eye1_center.draw(window)
    eye2_center.draw(window)
    eyebrow1.draw(window)
    eyebrow2.draw(window)
    mouth.draw(window)

    
def draw_cloud():
    draw_part(880, 250)
    draw_part(950, 250)
    draw_part(910, 200)
    draw_part(1020, 250)
    draw_part(980, 200)

def draw_part(x, y):
    part = gr.Circle(gr.Point(x, y), 40)
    part.setFill('white')

    part.draw(window)

def draw_background():
    sky= gr.Rectangle(gr.Point(0,0), gr.Point(1500, 450))
    sky.setFill('cyan')

    grass=gr.Rectangle(gr.Point(0,450), gr.Point(1500, 900))
    grass.setFill('green')

    sky.draw(window)
    grass.draw(window)

    
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

    
def draw_picture():
    draw_background()
    draw_sun()
    draw_sun_lines()
    draw_sun_face()
    draw_creature()
    draw_cloud()

draw_picture()

window.getMouse()

window.close()
    


    
