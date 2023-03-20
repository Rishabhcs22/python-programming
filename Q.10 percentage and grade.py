ph=int(input('enter the marks in physics:'))
ch=int(input('enter the marks in chemistry:'))
ma=int(input('enter the marks in mathematics:'))
bi=int(input('enter the marks in biology:'))
co=int(input('enter the marks in computer:'))
sum=ph+ch+ma+bi+co
percentage =sum/500*100
print('percentage',percentage)
if(percentage>=90):
    print("grade='A'")
elif(percentage>=80 and percentage<90):
    print("grade='B'")
elif(percentage>=70 and percentage<80):
    print("grade='C'")
elif(percentage>=60 and percentage<70):
    print("grade='D'")
elif(percentage>=40 and percentage<50):
    print("grade='E'")
else:
    print("grade='F'")

    



