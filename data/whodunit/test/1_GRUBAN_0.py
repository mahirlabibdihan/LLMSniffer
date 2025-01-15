
from math import sqrt, floor
def T(N):
    A=[]
    for i in range(1, floor(sqrt(N))+1):
        if N%i==0:
            if N//i==i:
                A.append(i)
            else:
                A.append(i)
                A.append(N//i)
    return A 
a=int(input())
for i in range(a):
    N, K=map(int, input().split())
    A=T(N)
    if N<(K*(K+1))//2:
        print(-1)
    else:
        B=[]
        for j in A:
            if N//j>=(K*(K+1))//2:
                B.append(j)
        b=max(B)
        print(b)