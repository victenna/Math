import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('gold')
t.hideturtle()
cord=((100,100),(300,100),(400,200),(200,400))
print(cord)
turtle.addshape('poly',cord)
s=turtle.Turtle(shape='poly')
s.up()
s.hideturtle()
s.goto(-200,-200)
s.showturtle()
s.color('blue')
s.tilt(90)

X=[1,3,4,2,1]
Y=[1,1,2,4,1]

Sum1=0
Sum2=0
for i in range(4):
    Sum1=Sum1+X[i]*Y[i+1]
    Sum2=Sum2+Y[i]*X[i+1]
    

Area=(Sum1-Sum2)/2

print(Area)

