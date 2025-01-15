from math import gcd

def solve(n):
    p = 10**n - 10**(n//2)
    q = 10**n
    g = gcd(p, q)
    return p//g, q//g

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p, q = solve(n)
    print(p, q)