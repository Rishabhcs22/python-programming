string = input("Enter a string: ")
substring = input("Enter a substring: ")

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        print("Substring found at position", i)
        break
else:
    print("Substring not found in the given string.")
