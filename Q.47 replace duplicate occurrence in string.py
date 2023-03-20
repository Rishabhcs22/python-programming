string = input("Enter a string: ")

new_string = ""
for i in range(len(string)):
    if string[i] not in new_string:
        new_string += string[i]
    else:
        new_string += "*"

print("Original string:", string)
print("New string:", new_string)
