number = int(input("Find prime numbers upto : "))
print("\nAll prime numbers upto", number, "are : ")
for num in range(2, number + 1):
    i = 2
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
    if(i != num):
        print(num, end=" ")
