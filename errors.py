try:
    a=100
    b=input()
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("abc")
