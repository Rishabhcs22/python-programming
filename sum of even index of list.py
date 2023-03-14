ls=[]
sum=0
x=int(input('enter the number of elements:'))
for i in range(0,x):
    y=int(input('enter the elements:'))
    ls.append(y)
print(ls)
for i in range(0,x):
    if(i%2==0):
        sum=sum+ls[i]
print('The sum of even index elements is:',sum)
