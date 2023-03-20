str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

count = 0

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            count += 1

print("Number of matching characters: ", count)
