
def add(n,m):
    x=n+m
    return x
def sub(n,m):
    x=n-m
    return x
def mult(n,m):
    x=n*m
    return x
def div(n,m):
    x=n/m
    return x


try:
    a=eval(input("enter first number: "))
    sign=input("enter operation: ")
    b=eval(input("enter second number: "))


    if sign=="+":
        p=add(a,b)
        print("answer is ",p)

    elif sign=="-":
        p=sub(a,b)
        print("answer is ",p)

    elif sign=="/":
        p=div(a,b)
        print("answer is ",p)

    elif sign=="*":
        p=mult(a,b)
        print("answer is ",p)

except ZeroDivisionError:
    print("cant divide by zero")


   