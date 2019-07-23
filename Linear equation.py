a = float(input("Coefficient a= "))
b = float(input("Coefficient b "))
if (a == 0 and b == 0):
    print("Infinity solution number")
if (a == 0 and b != 0):
    print("No solution")
if (a != 0):
    print('unique solution value=', b/a)
    #print('answer=',b/a)
