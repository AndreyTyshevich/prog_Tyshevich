import graphics as gr
import random

window = gr.GraphWin("pic", 1500, 900)


def draw_picture():
    draw_background()
    draw_sun()
    draw_sun_lines()
    draw_sun_face()
    draw_cloud()
    draw_creature()


def draw_background():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1500, 450))
    sky.setFill('cyan')

    grass = gr.Rectangle(gr.Point(0, 450), gr.Point(1500, 900))
    grass.setFill('green')

    sky.draw(window)
    grass.draw(window)


def draw_sun():
    sun = gr.Circle(gr.Point(180, 200), 100)
    sun.setFill('yellow')
    sun.draw(window)


def draw_sun_face():
    draw_eye(150, 180, 20, 'red')
    draw_eye(250, 180, 15, 'red')
    draw_eye_pupil(150, 180, 8)
    draw_eye_pupil(250, 180, 7)
    draw_eyebrow(100, 120, 180, 170)
    draw_eyebrow(220, 170, 300, 140)
    draw_mouth(150, 260, 250, 260, 'black')


def draw_mouth(x_bottom, y_bottom, x_top, y_top, colour):
    mouth = gr.Line(gr.Point(x_bottom, y_bottom), gr.Point(x_top, y_top))
    mouth.setWidth(20)
    mouth.setOutline(colour)
    mouth.draw(window)


def draw_eye(x, y, r, colour):
    eye = gr.Circle(gr.Point(x, y), r)
    eye.setFill(colour)
    eye.draw(window)


def draw_eye_pupil(x, y, r):
    pupil = gr.Circle(gr.Point(x, y), r)
    pupil.setFill('black')
    pupil.draw(window)


def draw_eyebrow(x_bottom, y_bottom, x_top, y_top):
    eyebrow = gr.Line(gr.Point(x_bottom, y_bottom), gr.Point(x_top, y_top))
    eyebrow.setWidth(10)
    eyebrow.setOutline('black')
    eyebrow.draw(window)


def draw_sun_lines():
    for x in range(1000):
        draw_sun_line(random.randint(50, 500), random.randint(50, 500))
        

def draw_sun_line(x, y):
    sunline = gr.Line(gr.Point(150, 180), gr.Point(x, y))
    sunline.setFill('yellow')
    sunline.draw(window)


def draw_cloud():
    for x, y in (880, 250), (950, 250), (1020, 250), (910, 200), (980, 200):
        draw_small_cloud(x, y)


def draw_small_cloud(x, y):
    cloud = gr.Circle(gr.Point(x, y), 40)
    cloud.setFill('white')
    cloud.draw(window)


def draw_creature():
    face = gr.Circle(gr.Point(700, 500), 100)
    face.setFill('pink')
    face.draw(window)

    draw_eye(650, 480, 20, 'white')
    draw_eye(710, 480, 20, 'white')
    draw_eye_pupil(650, 480, 8)
    draw_eye_pupil(710, 480, 7)
    draw_mouth(700, 550, 710, 580, 'white')
    draw_leg(650, 620, 680, 550)
    draw_leg(750, 620, 720, 550)


def draw_leg(x_bottom, y_bottom, x_top, y_top):
    leg = gr.Line(gr.Point(x_bottom, y_bottom), gr.Point(x_top, y_top))
    leg.setWidth(20)
    leg.setOutline('pink')
    leg.draw(window)


draw_picture()

window.getMouse()

window.close()
