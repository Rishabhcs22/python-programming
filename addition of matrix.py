row=int(input('enter the rows:'))
col=int(input('enter the column:'))
ls=[]
ls2=[]
ls4=[]
for i in range(0,row):
    ls1=[]
    for j in range(0,col):
        y=int(input())
        ls1.append(y)
    ls.append(ls1)
print(ls)
for i in range(row):
    for j in range(col):
        print(ls[i][j], end=' ')
    print()
print('second matrix')
for i in range(0,row):
    ls3=[]
    for j in range(0,col):
        x=int(input())
        ls3.append(x)
    ls2.append(ls3)
print(ls2)
for i in range(row):
    for j in range(col):
        print(ls2[i][j], end=' ')
    print()
print('addition of matrix')
for i in range(row):
    for j in range(col):
        print(ls[i][j]+ls2[i][j], end=' ')
    print()
