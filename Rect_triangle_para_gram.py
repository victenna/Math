import turtle,time
turtle.hideturtle()
t1=turtle.Turtle()
t1.hideturtle()
t2=turtle.Turtle()
t2.hideturtle()
wn=turtle.Screen()
wn.setup(1300,1000)
turtle.bgcolor('light blue')
text=turtle.Turtle()
text.color('blue')
text.hideturtle()
text.up()
text.goto(-300,400)
TEXT_FONT=('Arial',25,'bold')
text.write('AREA FINDER', font=TEXT_FONT)
TEXT_FONT=('Arial',20,'bold')
text.goto(-300,350)
text.write('Rectangle Area, choose one', font=TEXT_FONT)
text.goto(-300,300)
text.write('Triangle Area, choose two', font=TEXT_FONT)
text.goto(-300,250)
text.write('Parallelogram Area, choose three', font=TEXT_FONT)


image1=('rectangle.gif')
image2=('triangle.gif')
image3=('para_gram.gif') #down load image parallelogram from internet to your computer (the same directory, where youe execute file)

def img(image):
    
    wn.addshape(image)
    t1.shape(image)

t1.up()
t1.goto(-200,0)
t1.showturtle()
    
def triangle():
    global base
    global h
    global Area
    base=float(wn.textinput('Triangle Area','Base='))
    h = float(wn.textinput('Triangle Area','Height='))
    Area=base*h/2
    print(Area)
    turtle.clear()

def rectangle():
    global base
    global h
    global Area
    base = float(wn.textinput('Rectangle Area','Base='))
    h = float(wn.textinput('Rectangle Area','Height='))
    Area=base*h
    print(Area)
    turtle.clear()
    
   
def parall_m():
    
    global base
    global h
    global Area
    base = float(wn.textinput('Parallelogram Area','Base='))
    h = float(wn.textinput('Parallelogram Area','Height='))
    Area=base*h
    print(Area)
    turtle.clear()
    
def spec(X1,Y1, X2,Y2, Z,str_name):

    turtle.up()
    turtle.color('blue')
    turtle.goto(X1,Y1)
    turtle.down()
    turtle.write(str_name,font=('Times New Roman',20,'bold'))
    turtle.up()
    turtle.goto(X2,Y2)
    turtle.write(Z, font=('Times New Roman',20,'bold'))
   
answer=wn.textinput('Choose Area number','one or two or three')
if answer=='one':
    t1.clear()
    img(image1)
    rectangle()
if answer=='two':
    t1.clear()
    img(image2)
    triangle()
if answer=='three':
    t1.clear()
    img(image3)
    parall_m()

spec(210,0,280,0,base,'base=')

spec(210,-30,250,-30,h,'h=')
spec(400,0,470,0,Area,'Area=')

while True:

    answer=wn.textinput('Want to continue','yes or no')
    
   
    if answer=='yes':
        turtle.clear()

        answer=wn.textinput('Choose Area number','one or two or three')
        if answer=='one':
            t1.clear()
            img(image1)
            rectangle()
        if answer=='two':
            t1.clear()
            img(image2)
            triangle()
        if answer=='three':
            t1.clear()
            img(image3)
            parall_m()
        turtle.clear()
      
        spec(210,0,280,0,base,'base=')
        spec(210,-30,250,-30,h,'h=')
        spec(400,0,470,0,Area,'Area=')
               
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


        
