row=int(input('enter the rows:'))
col=int(input('enter the column:'))
ls=[]
ls1=[]
for i in range(0,row):
    for j in range(0,col):
        y=int(input())
        ls1.append(y)
    ls.append(ls1)
print(ls)
for i in range(row):
    for j in range(col):
        print(ls[i][j], end=' ')
    print()

    
