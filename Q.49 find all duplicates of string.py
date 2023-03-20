string = input('enter the string:')
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
for char in char_freq:
    if char_freq[char] > 1:
        print(char)
