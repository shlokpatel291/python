list1=[]
for i in range(1,21):
    list1.append(i)
print(list1)


list2=[]


for i in range(0,11):
    x=list1[i]
    if x%2==0:
        list2.append(x)
        list1.remove(x)


print("list1 is:",list1)
print("list 2 is:",list2)
