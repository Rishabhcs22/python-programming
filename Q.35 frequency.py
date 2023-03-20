string =input('enter the string:')
words = string.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
for word, count in freq.items():
    print(word, count)
