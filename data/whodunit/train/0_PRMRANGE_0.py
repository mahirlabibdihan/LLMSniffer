from collections import defaultdict
from math import sqrt

def prime_factors(n):
    i = 2
    factors = defaultdict(int)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors

def solve():
    K, Q = map(int, input().split())
    K_factors = prime_factors(K)
    A = [defaultdict(int) for _ in range(10**5 + 1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l, r = query[1], query[2]
            count = 0
            for factor in K_factors:
                for i in range(l, r + 1):
                    if A[i][factor] > 0:
                        count += 1
                        break
            print(count)
        else:
            l, r, x = query[1], query[2], query[3]
            x_factors = prime_factors(x)
            for i in range(l, r + 1):
                for factor in x_factors:
                    A[i][factor] += 1

solve()