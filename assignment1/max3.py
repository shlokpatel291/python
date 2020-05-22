x,y,z=input("enter three numbers").split()


if x>y:
    if x>z:
        max=x
    else:
        max=z
else:
    if y>z:
        max=y
    else:
        max=z


print("maximum=",max)