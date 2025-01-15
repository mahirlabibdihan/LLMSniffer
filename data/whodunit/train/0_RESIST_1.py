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
    else:
        return (power(2, n - 2, m) * (power(2, n - 1, m) - 1)) % m

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    P = solve(N, M)
    Q = power(2, N - 1, M)
    Q_inv = modInverse(Q, M)
    if Q_inv == -1:
        print("Not exist")
    else:
        print((P * Q_inv) % M)