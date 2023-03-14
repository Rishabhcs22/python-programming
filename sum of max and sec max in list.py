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
        sec_max=temp
        temp=i
print(temp)
print(sec_max)
sum=temp+sec_max
print('The sum of maximum and second maximum element in list is:',sum)
