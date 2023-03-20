upto=int(input('enter armstrong numbers you want upto:'))
print('The armstrong number upto',upto,'are:')
for i in range(150,upto+1):
    temp=i
    sum=0
    while(temp>150):
      digit=temp%10
      sum=sum+(digit**3)
      temp=temp//10
      if(i==sum):
          print(i)
'''i=152
sum=0
while (i<upto):
    d=i%10
    sum=sum+(d**3)
    i=i//10
    i+=1
    if (i==sum):
        print(i)
    else:
        print("none"'''

