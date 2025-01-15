from math import ceil,sqrt
l=[0]*(10**6+1)
for i in range(2,10**6):
    if l[i]==0:
        j=1
        while (i*j)<=(10**6):
            l[i*j]+=1
            j+=1
for i in range(int(input())):
    n,m=map(int,input().split())
    c=0
    for i in range(n,m):
        c+=l[i]
    print(c)
