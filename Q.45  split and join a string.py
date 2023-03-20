input_str = input('enter the string:')
split_str = []
temp_str = ""
for i in input_str:
    if i == " ":
        split_str.append(temp_str)
        temp_str = ""
    else:
        temp_str += i
split_str.append(temp_str)
join_str = ""
for i in range(len(split_str)):
    join_str += split_str[i]
    if i != len(split_str) - 1:
        join_str += " "
print("Input String:", input_str)
print("Split String:", split_str)
print("Joined String:", join_str)
