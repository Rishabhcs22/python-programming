num =int(input('enter the number'))
n1, n2 = 0, 1
if(num==0):
    print(n1)
elif(num<=0):
    print('number should be positive')
else:
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

print()
