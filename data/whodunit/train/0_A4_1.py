import math

def solve(n, k):
    a = pow(10, k)
    b = pow(n, n, a)
    c = pow(10, k - 1)
    d = int(str(pow(n, n))[:k])
    return d, b if b > c else b + a

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    first, last = solve(n, k)
    print(first, last)