import random
ls=[]
for i in range(1,101):
    ls1=random.randint(1000000000,9999999999)
    if ls1 not in ls:
        ls.append(ls1)
print(ls)
print()

