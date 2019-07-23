import turtle,time
import math
t=turtle.Turtle()
wn=turtle.Screen()
image='cylinder.gif'
wn.addshape(image)
t.shape(image)
t1=turtle.Turtle()
t1.up()
t1.hideturtle()
Text_font=('Arial',20,'bold')
pi=math.pi
for s in range (10):
    
    height=float(wn.textinput('Cube volume','Height of cylinder: '))
    radius=float(wn.textinput('Cube volume','Radius of cylinder: '))
    volume = height*pi * radius**2
    sur_area = 2*pi*radius * height + 2*pi*radius**2
    t1.goto(-300,-350)
    t1.color('blue')
    t1.write('Volume=',font=Text_font)
    t1.goto(-150,-350)
    t1.write(round(volume,1),font=Text_font)
    t1.goto(0,-350)
    t1.write('Surface Area=',font=Text_font)
    t1.goto(200,-350)
    t1.write(round(sur_area,1),font=Text_font)
    time.sleep(3)
    t1.clear()
wn.bye()

