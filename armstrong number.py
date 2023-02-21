number=int(input("enter any number="))
y=number
sum=0
while number!=0:
    digit=number%10
    sum=sum+(digit**3)
    number//=10
print('number is armstrong') if(y==sum) else print('number is not armstrong')
    
    
