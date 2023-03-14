ls=[]
temp=0
x=int(input('enter the number of elements:'))
for i in range(0,x):
    y=int(input('enter the elements:'))
    ls.append(y)
print('user entered list:',ls)
temp=ls[-1]
ls[-1]=ls[0]
ls[0]=temp
print('list after interchanging first and last element',ls)
