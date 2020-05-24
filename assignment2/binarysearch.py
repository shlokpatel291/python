def search(s):
    
    l=len(arr)
    for i in range(0,l):
        if arr[i]==s:
            print (s,"is at position",i+1)
            break


arr=[1,3,5,7,9]
element=7
search(element)
