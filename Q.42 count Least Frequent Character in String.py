string = input('enter the string:')
char_counts = {}
for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
least_freq_char = None
least_freq_count = len(string)
for char, count in char_counts.items():
    if count < least_freq_count:
        least_freq_char = char
        least_freq_count = count
print(f"The least frequent character in the string is '{least_freq_char}' with a count of {least_freq_count}.")
