import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('lightblue')
t.hideturtle()
t.pensize(5)

t.color('red')

def line(x,y,length,angle):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()
    t.pendown()
    t.fd(length)
    t.penup()
line(-183,-30,400,0)
line(-183,30,400,0)
line(-150,-100,300,45)
line(-50,-100,300,45)

    
