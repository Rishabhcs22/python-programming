snake_case_string = input('enter the snake case string:')
pascal_case_string = ""

for word in snake_case_string.split("_"):
    pascal_case_string += word.capitalize()

print(pascal_case_string)
