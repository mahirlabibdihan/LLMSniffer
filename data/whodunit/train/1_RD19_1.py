from math import gcd
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=gcd(l[0],l[1])
    for i in range(len(l)):
       gcd1=gcd(a,l[i])
    if(gcd1==1):
       print(0)
    else:
       print(-1)