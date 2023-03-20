str_input = input("Enter a string: ")
char_freq = {}
for char in str_input:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
max_freq = 0
max_char = ''
for char in char_freq:
    if char_freq[char] > max_freq:
        max_freq = char_freq[char]
        max_char = char
print("The character with maximum frequency is:", max_char)
