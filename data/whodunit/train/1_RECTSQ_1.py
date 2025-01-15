import math
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=math.gcd(n,m)
    n1=int(n/a)
    n2=int(m/a)
    print(n1*n2)