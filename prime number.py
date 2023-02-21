number=int(input('enter any number='))
count=0
y=2
while number>1:

    if(number%y==0):
        count=count+1
    else:
        break
    y+=1
   
if count>0:
    print('number is not a prime number')
else:
    print('number is a prime number')