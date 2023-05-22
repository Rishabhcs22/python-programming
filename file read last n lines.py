f=open("py.txt",'r')
y=len("py.txt")
n=int(input())
for i in range(y,n,-1):
    x=f.readline()
    print(x)
f.close()
