# Parallelogram area
import turtle
turtle.hideturtle()
t1=turtle.Turtle()
t2=turtle.Turtle()

import time
wn=turtle.Screen()
wn.setup(1000,500)
image=('para_gram.gif') #down load image parallelogram from internet to your computer (the same directory, where youe execute file)
wn.addshape(image)
t1.shape(image)
t1.up()
t1.hideturtle()
t1.goto(300,0)
t1.showturtle()
t2.up()
t2.goto(150,200)
t2.hideturtle()
t2.write('PARALLELOGRAM AREA', font=('Times New Roman', 20 ,'bold'))


def parall_m():
    

    base = int(input('Parallelogram base ='))
    h = int(input('Parallelogram height h='))
    Area=base*h
    print(Area)

    turtle.clear()
    turtle.up()
    turtle.color('blue')
    turtle.goto(170,0)
    turtle.down()
    turtle.write('base=',font=('Times New Roman',20,'bold'))
    turtle.up()
    turtle.goto(240,0)
    turtle.write(base, font=('Times New Roman',20,'bold'))
    #turtle.hideturtle()

    
    #turtle.up()
    turtle.color('blue')
    turtle.goto(170,-30)
    turtle.down()
    turtle.write('h=',font=('Times New Roman',20,'bold'))
    turtle.up()
    turtle.goto(210,-30)
    turtle.write(h, font=('Times New Roman',20,'bold'))
    #turtle.hideturtle()

    
    turtle.up()
    turtle.color('blue')
    turtle.goto(300,0)
    turtle.down()
    turtle.write('Area=',font=('Times New Roman',20,'bold'))
    turtle.up()
    turtle.goto(370,0)
    turtle.write(Area, font=('Times New Roman',20,'bold'))
    #turtle.hideturtle()

parall_m()

while True:
   answer=input("Do you want to continue calculations:yes or no")
   if answer=='yes':
       parall_m()
               
   if answer=='no':
         turtle.clear()
         t1.hideturtle()
         t2.clear()
      
         print("CALCULATION OVER")
         turtle.color('red')
         
         turtle.hideturtle()
         turtle.goto(-200,0)
         turtle.write('THE END', font=('Times New Roman',105,'bold'))
         time.sleep(5)      
         break

        
   
