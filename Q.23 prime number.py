num=int(input('enter any number:'))
count=0
for i in range(2,num+1):
    if(num%i==0):
        count+=1
if(count==1):
    print('number is a prime number')
else:
    print('number is not a prime number')
