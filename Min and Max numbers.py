#code evaluates minimum and maximum among the list values 
a=[]
n=int(input('How many terms n do you want to use to find max and min value  '))

while len(a)<n:
    a.append(int(input('input value:  ')))
print('min value=',min(a))
print('min value=',max(a))

print('numbers=',a)
