input_string = input('enter the string:')
output_string = ""
for char in input_string:
    if char not in output_string:
        output_string += char
print(output_string)
