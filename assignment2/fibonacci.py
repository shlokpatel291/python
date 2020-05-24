i=1
def fibo(n):
    if n<=1:
        return n 
    else:
        return(fibo(n-1)+fibo(n-2))

nterms=10

for i in range(0,nterms):
    print(fibo(i),"\n")