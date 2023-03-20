number = int(input("Find prime numbers upto : "))
sum=0
print("\nAll prime numbers upto", number, "are : ")
for num in range(2, number + 1):
    i = 2
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
    if(i != num):
        print(num, end=" ")
        sum=sum+num
print("\nsum of the prime numbers upto",number,"is:",sum)
