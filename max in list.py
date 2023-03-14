ls=[]
temp=0
x=int(input('enter the number of elements:'))
for i in range(0,x):
    y=int(input('enter the elements:'))
    ls.append(y)
print(ls)
temp=ls[0]
for i in ls:
    if temp<i:
        temp=i
print('The maximum element in the list is:',temp)
