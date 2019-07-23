# quadratic equation
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: this program crashes if the equation has no real roots.

import math  # Makes the math library available.
import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('gold')
Text_font=('Arial', 30,'bold')
t.up()
t.color('blue')
t.hideturtle()
t.goto(-300,0)
t.write('Quadratic Equation: Ax^2+Bx+C=0',font=Text_font)
def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    q=b * b - 4 * a * c
    if q>=0:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("The solutions are:", root1, root2 )
    else:
        print('No solution')
        

    #print()
    

main()
