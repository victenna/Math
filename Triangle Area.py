import turtle,time
import math
t=turtle.Turtle()
wn=turtle.Screen()
image='Triangle.gif'
wn.addshape(image)
t.shape(image)
t1=turtle.Turtle()
t1.up()
t1.hideturtle()
Text_font=('Arial',20,'bold')
for s in range (10):
    
    height=float(wn.textinput('Triangle Area','Height of triangle: '))
    base=float(wn.textinput('Triangle Area','Base: '))
    area = height*base/2
    t1.goto(-100,-350)
    t1.color('blue')
    t1.write('Area=',font=Text_font)
    t1.goto(-20,-350)
    t1.write(round(area,1),font=Text_font)
    time.sleep(5)
    t1.clear()

"""
    t1.goto(0,-350)
    t1.write('Area=',font=Text_font)
    t1.goto(200,-350)
    t1.write(round(sur_area,1),font=Text_font)
    time.sleep(3)
    t1.clear()
"""
wn.bye()


