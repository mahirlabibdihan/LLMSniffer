import math
T=int(input())
for  _ in range(T):
    N,M=map(int,input().split())
    a=N*(N+1)//2
    b=(a+M)//2
    c=a-b
    if b-c ==M:
        if math.gcd(b,c) ==1.0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")