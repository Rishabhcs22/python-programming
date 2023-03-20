number=int(input('enter any number='))
y=number
reverse_number=0
while number!=0:
    digit=number%10
    reverse_number=reverse_number*10+digit
    number//=10
if(y==reverse_number):
    print("The number you entered is a palindrome")
else:
    print("The number you entered is not a palindrome")
    
