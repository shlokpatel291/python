x,y=input("enter start and end").split()
a=eval(x)
b=eval(y)
for p in range(a,b+1):
    if p in [1,2,3,5,7]:
        print(p)
    if p>9:
         if p%2 !=0 and p%3 !=0 and p%5 !=0 and p%7 !=0 :
            print(p) 