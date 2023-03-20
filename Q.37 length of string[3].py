def count_chars(string):
    if string == '':
        return 0
    else:
        return 1 + count_chars(string[1:])

string = input('enter the string:')
print(count_chars(string))
