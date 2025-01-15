"""import math
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    d=[int(x) for x in input().split()]
    q=[int(y) for y in input().split()]
    res=1
    for i in range(len(q)):
        res=q[i]
        for j in range(len(d)):
            res=(res//d[j])
            
        print(res,end=' ')
    print()"""
t=int(input())
for i in range(t):
    n,q=map(int,input().split(' '))
    d=list(map(int,input().split()))
    Q=list(map(int,input().split()))
    j=1
    for k in d:
        j*=k
    for i in Q:
        x=i//j
        print(x,end=" ")
    print("")    