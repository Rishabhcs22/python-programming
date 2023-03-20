num=int(input('enter any number:'))
count=0
print("factors are:")
for i in range(1,num+1):
    if(num%i==0):
        print(i,end="  ")
        count+=1
print()
print("no of factors are:",count)
    
