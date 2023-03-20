import math
num=int(input("enter value:"))
sum=0
temp=num
while(temp>0):
    d=temp%10
    fact=math.factorial(d)
    temp=temp//10
    sum=sum+fact
if sum==num:
    print(" strong number ")
else :
    print("not a strong numer ")

