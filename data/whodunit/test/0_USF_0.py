from collections import defaultdict
from math import sqrt
from sys import stdin, stdout

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    primes = defaultdict(int)
    for x in a:
        for p in prime_factors(x):
            primes[p] += 1
    primes = sorted(primes.values(), reverse=True)
    ans = max(primes)
    for i in range(1, len(primes)):
        ans = max(ans, (i+1)*primes[i])
    stdout.write(str(ans) + '\n')

t = int(stdin.readline())
for _ in range(t):
    solve()