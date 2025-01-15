from fractions import Fraction
from math import gcd

def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    if y % 2 == 0:
        return p
    else:
        return ((x * p) % m)

def modInverse(a, m):
    g = gcd(a, m)
    if g != 1:
        return -1
    else:
        return power(a, m - 2, m)

def solve(n, m):
    if n == 1:
        return 1 % m
    elif n == 2:
        return 2 * modInverse(3, m) % m
    else:
        return (2 * modInverse(3, m) + (n - 2) * modInverse(2, m)) % m

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))