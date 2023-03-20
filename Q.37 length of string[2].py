string = input('enter the string:')
count = 0
while string:
    string = string[1:]
    count += 1
print(count)
