t=int(input())
for i in range(t):
    n,m=[int(x) for x in input().split()]
    l=[0]*m
    for x in range(n):
        z=input()
        for y in range(m):
            if z[y]=='1':
                l[y]+=1 
    a=0
    #print(l)
    for x in range(m):
        if (l[x]>1):
         a=a+((l[x]*(l[x]-1))//2)
         #print(a)
    print(a)    