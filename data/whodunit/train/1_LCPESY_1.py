from collections import *
for u in range(int(input())):
    s=input()
    r=input()
    x=Counter(s)
    y=Counter(r)
    c=0
    for i in x:
        c+=min(x[i],y[i])
    print(c)
