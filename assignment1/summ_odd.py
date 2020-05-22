sum=0
list1=[]
for i in range(1,101):
    if i%2 !=0:
        sum+=i
        list1.append(i)
print(sum)
print(list1)