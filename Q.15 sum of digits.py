num=int(input('enter the number:'))
sum=0
while num!=0:
    digit=num%10
    sum=sum+digit
    num//=10
print('sum of the digits:',sum)
    
