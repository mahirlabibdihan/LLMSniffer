import math 
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    g=0
    for i in range(n):
        g=math.gcd(a[i],g)
    print(g*n)
            