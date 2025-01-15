import math

t = int(input())

def result(n,k):
    m = min(n-k, k)
    u = 1
    for i in range(m):
        u*=(n-i)
    return u//math.factorial(m)

while t>0:
    n, k = list(map(int, input().strip().split(' ')))
    print(result(n-1, k-1))
    t=t-1