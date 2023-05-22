try:
    a=100
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("value error")
except TypeError:
    print("type error")
