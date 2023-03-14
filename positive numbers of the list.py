ls=[]
temp=0
x=int(input('enter the number of elements:'))
for i in range(0,x):
    y=int(input('enter the elements:'))
    ls.append(y)
print('user entered list:',ls)
for i in range(0,x):
    if(ls[i]>0):
        print('the positive numbers of the list is:',ls[i])
