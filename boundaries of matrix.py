row=int(input('enter the rows:'))
col=int(input('enter the column:'))
ls=[]
for i in range(0,row):
    ls1=[]
    for j in range(0,col):
        y=int(input())
        ls1.append(y)
    ls.append(ls1)
print(ls)
'''
for i in range(row):
    for j in range(col):
        print(ls[i][j], end=' ')
    print()
'''
print('Boundaries of the matrix')
for i in range(0,row):
       for j in range(0,col):
           if(j==0 or i==0 or j==row-1 or i==row-1):
              print(ls[i][j], end=" ")
           else:
              print(' ',end=" ")
       print()
    

    
