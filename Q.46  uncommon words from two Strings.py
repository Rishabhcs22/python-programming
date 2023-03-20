str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
words1 = str1.split()
words2 = str2.split()
unique_words = set(words1 + words2)
uncommon_words = []
for word in unique_words:
    if (word not in words1) or (word not in words2):
        uncommon_words.append(word)
print("Uncommon words:", uncommon_words)
