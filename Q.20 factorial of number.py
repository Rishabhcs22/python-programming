num=int(input('Enter any number:'))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print("factorial of ",num, 'is:',fact)
