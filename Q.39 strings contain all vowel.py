vowels = {'a', 'e', 'i', 'o', 'u'}
input_string = input("Enter a string: ")
string_set = set(input_string.lower())

if vowels.issubset(string_set):
    print("The input string contains all vowels.")
else:
    print("The input string does not contain all vowels.")
