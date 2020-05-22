line=input("enter the sentence:")
count=0

for i in line:
    if(i.isspace()):
        count+=1
print("number of space=",count)

