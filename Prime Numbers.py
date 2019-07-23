#Check: prime number or not
def prime_number(x):
    global n
    if x >= 2:
        
        for y in range(2,x):
            
            k=x%y
            
            if k==0:
                n=0
                print('usual')
                break
            n=1      
forward=True

while forward:
    answer=input("Do you want to find prime number? yes or no\n")
    
    if answer=='no':
        break
    
    q= input("Please enter a number:\n")    
    a=int(q)
    prime_number(a)

    if n==1:
        print('prime')

