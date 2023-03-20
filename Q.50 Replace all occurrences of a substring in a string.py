string = input('enter the string:')
sub_string = "o"
replace_with = "x"
chars = list(string)
for i in range(len(chars)):
    if chars[i:i+len(sub_string)] == list(sub_string):
        chars[i:i+len(sub_string)] = list(replace_with)
new_string = "".join(chars)
print(new_string)
