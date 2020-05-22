x="the quick brown fox jumps over the lazy dog"
p=x.split()
l=len(p)
for i in range(0,l):
    if p[i] !=" ":
        t=p[i]
        y=t.split()
       
        word=y[0]
        fletter=s[:1]
        print(fletter)