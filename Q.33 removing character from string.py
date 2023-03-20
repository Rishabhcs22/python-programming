string = input('enter the string:')
i = int(input('enter the index want to remove'))
new_string = ""
for j in range(len(string)):
    if j != i:
        new_string += string[j]

print(new_string)
