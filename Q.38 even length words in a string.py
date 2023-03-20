string = input("Enter a string: ")  
words = string.split()  
even_length_words = []
for word in words:
    if len(word) % 2 == 0:  
        even_length_words.append(word)
        print("Even length words in the string:", ", ".join(even_length_words))

    else:
        print('odd')
