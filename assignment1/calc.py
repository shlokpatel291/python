a=eval(input("enter first number:"))
b=eval(input("enter second number:"))
x=input("enter operation:")

if x=="*":
    print(a*b)
elif x=="/":
    if b !=0:
        print(a/b)
    else:
        print("cant divide by zero")
elif x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
elif x=="%":
    if b!=0:
        print(a%b)
    else:
        print("error")