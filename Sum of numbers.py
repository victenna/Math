#code evaluates sum of chosen numbers
a=[]
n=int(input('How many terms n do you want to use for sum  '))

while len(a)<n:
    a.append(int(input('input value:  ')))
#print('min value=',max(a))
print('numbers=',a)

numbers1=[]
numbers2=[]
numbers3=[]
numbers4=[]

for i in range(n):
    #print (a[i])
    numbers1.append(a[i])
    numbers2.append(a[i]**2)
    numbers3.append(a[i]**3)
    numbers4.append(a[i]**4)
        
        
print('sum of numbers=', sum(numbers1))
print('sum of numbers=', sum(numbers2))
print('sum of numbers=', sum(numbers3))
print('sum of numbers=', sum(numbers4))


    
    
    

