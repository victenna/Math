a = int(input('triangle length a=  '))
       
b = int(input('triangle length b=  '))
c = int(input('triangle length c=  '))
if (a + b) <= c or (a + c) <= b or (c + b) <= a or a + b + c <= 0:
    print("impossible")
else:
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 > 0:
        print("acute")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 > 0:
        print("acute")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 > 0:
        print("acute")
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 < 0:
        print("obtuse")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 < 0:
        print("obtuse")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 < 0:
        print("obtuse")
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 == 0:
        print("right")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 == 0:
        print("right")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 == 0:
        print("right")
