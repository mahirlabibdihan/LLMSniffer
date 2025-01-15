import math

def solve(n, k):
    a = pow(10, k)
    b = pow(n, n, a)
    c = pow(10, k - 1)
    d = n ** n
    while d >= c:
        d /= 10
    return int(d), b

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    first, last = solve(n, k)
    print(first, last)