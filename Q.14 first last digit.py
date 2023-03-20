num = int(input('Enter any Number: '))
temp=num
while(num>=10):
    num = num // 10
print('THe first digit of the number is:',num)
last=temp%10
print('The last digit of the number is:',last)
