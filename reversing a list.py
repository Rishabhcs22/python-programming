ls=[]
temp=0
x=int(input('enter the number of elements:'))
for i in range(0,x):
    y=int(input('enter the elements:'))
    ls.append(y)
print('user entered list:',ls)
print('after reversing the string')
ls_2=ls[ : :-1]
print(ls_2)
