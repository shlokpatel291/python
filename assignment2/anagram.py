def anagram(a,b):
    list1=list(a)
    list2=list(b)
    sort1=list1.sort()
    sort2=list2.sort()
    if sort1==sort2:
        print("it is anagram")
    else:
        print("not an anagram")


str1=input("enter the first word: ")
str2=input("enter the second word: ")

anagram(str1,str2)