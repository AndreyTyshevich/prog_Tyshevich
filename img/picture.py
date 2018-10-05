import graphics as gr

window = gr.GraphWin("pic", 1500, 900)

sun = gr.Circle(gr.Point(180, 200), 100)
sun.setFill('yellow')

sunline1 = gr.Line(gr.Point(150, 180), gr.Point(450, 180))
sunline1.setFill('yellow')

sunline2 = gr.Line(gr.Point(150, 180), gr.Point(420, 200))
sunline2.setFill('yellow')

sunline3 = gr.Line(gr.Point(150, 180), gr.Point(390, 280))
sunline3.setFill('yellow')

sunline4 = gr.Line(gr.Point(150, 180), gr.Point(370, 250))
sunline4.setFill('yellow')

sunline5 = gr.Line(gr.Point(150, 180), gr.Point(350, 230))
sunline5.setFill('yellow')

sunline6 = gr.Line(gr.Point(150, 180), gr.Point(330, 200))
sunline6.setFill('yellow')

sunline7 = gr.Line(gr.Point(150, 180), gr.Point(300, 290))
sunline7.setFill('yellow')

sunline8 = gr.Line(gr.Point(150, 180), gr.Point(290, 250))
sunline8.setFill('yellow')

sunline9 = gr.Line(gr.Point(150, 180), gr.Point(250, 280))
sunline9.setFill('yellow')

sunline10 = gr.Line(gr.Point(150, 180), gr.Point(230, 350))
sunline10.setFill('yellow')

sunline11 = gr.Line(gr.Point(150, 180), gr.Point(200, 370))
sunline11.setFill('yellow')

sunline12 = gr.Line(gr.Point(150, 180), gr.Point(100, 450))
sunline12.setFill('yellow')

sky= gr.Rectangle(gr.Point(0,0), gr.Point(1500, 450))
sky.setFill('cyan')

grass=gr.Rectangle(gr.Point(0,450), gr.Point(1500, 900))
grass.setFill('green')


cloud1 = gr.Circle(gr.Point(880, 250), 40)
cloud1.setFill('white')
cloud2 = gr.Circle(gr.Point(950, 250), 40)
cloud2.setFill('white')
cloud3 = gr.Circle(gr.Point(910, 200), 40)
cloud3.setFill('white')
cloud4 = gr.Circle(gr.Point(1020, 250), 40)
cloud4.setFill('white')
cloud5 = gr.Circle(gr.Point(980, 200), 40)
cloud5.setFill('white')


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



sky.draw(window)
grass.draw(window)
sun.draw(window)
sunline1.draw(window)
sunline2.draw(window)
sunline3.draw(window)
sunline4.draw(window)
sunline5.draw(window)
sunline6.draw(window)
sunline7.draw(window)
sunline8.draw(window)
sunline9.draw(window)
sunline10.draw(window)
sunline11.draw(window)
sunline12.draw(window)

cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)

face2.draw(window)
eye1.draw(window)
eye2.draw(window)
eye1_center.draw(window)
eye2_center.draw(window)
eyebrow1.draw(window)
eyebrow2.draw(window)
mouth.draw(window)

eye3.draw(window)
eye4.draw(window)
eye3_center.draw(window)
eye4_center.draw(window)
mouth2.draw(window)

leg1.draw(window)
leg2.draw(window)

window.getMouse()

window.close()
