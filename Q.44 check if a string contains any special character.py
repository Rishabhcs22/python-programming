special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '/', '?', '<', '>'}
string = input("Enter a string: ")
contains_special_char = False
for char in string:
    if char in special_chars:
        contains_special_char = True
        break
if contains_special_char:
    print("The string contains at least one special character.")
else:
    print("The string does not contain any special characters.")
