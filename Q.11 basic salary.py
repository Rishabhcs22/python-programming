Salary=int(input('enter the basic salary:'))
if(Salary <= 10000):
    print("HRA = 20% & DA = 80%")
elif(Salary <= 20000):
    print("HRA = 25% & DA = 90%")
elif(Salary > 20000):
    print("HRA = 30% & DA = 95%")
else:
    print("please enter valid salary details")
