number=int(input('enter the number='))
y=number
reverse_number=0
while number!=0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number//=10
    
print('number is palindrome') if(reverse_number == y) else print('number is not palindrome')
