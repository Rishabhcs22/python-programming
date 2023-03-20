n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
a = 0
b = 1
count = 0
while True:
    if b % m == 0:
        count += 1
        if count == n:
            print("The", n, "th multiple of", m, "in the Fibonacci series is", b)
            break
    c = a + b
    a = b
    b = c
