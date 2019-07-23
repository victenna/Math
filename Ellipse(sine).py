import math
import turtle
wn=turtle.Screen()
wn.setup(1000,1000)
wn.bgcolor('blue')
t=turtle.Turtle()
t.hideturtle()
turtle.tracer(1)
t.up()
t.speed(0)
pi=3.14159
#a=100
#b=70
a= int(wn.textinput("Ellipse Drawing", \
                              "semi-major ellipse axis value= "))

b= int(wn.textinput("Ellipse Drawing", \
                              "semi-minor ellipse axis value= "))

t.goto(a,0)
t.down()
t.color('red')
t.begin_fill()

for i in range(51):
    x=a*math.cos(0.04*i*pi)
    y=b*math.sin(0.04*i*pi)
    t.setposition(x,y)
    
t.end_fill()
