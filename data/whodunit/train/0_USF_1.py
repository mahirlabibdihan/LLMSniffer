import math
from collections import defaultdict

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    primes = defaultdict(int)
    for i in range(n):
        factors = set(prime_factors(a[i]))
        for f in factors:
            primes[f] += 1
    print(max(primes.values()))

t = int(input())
for _ in range(t):
    solve()
