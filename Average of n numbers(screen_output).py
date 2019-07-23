#The average of n numbers
import turtle
val=turtle.Turtle()
val.hideturtle()
val.up()
Text_font=('Arial',20,'bold')
wn=turtle.Screen()

n= int(wn.textinput("Average Estimation", \
                              "How many numbers n do you want to average"))

print(n)
sum=0
for j in range(n):
    value= int(wn.textinput('Average Estimation', \
                             'Enter value'))
    val.setposition(40*j,300)
    val.write(value,font=Text_font)
    
    sum=sum+value
average=sum/n
val.setposition(0,200)
val.write('average=',font=Text_font)
val.setposition(120,200)
val.write(average,font=Text_font)
print('average=', average)


