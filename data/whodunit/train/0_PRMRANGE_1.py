from collections import defaultdict
from math import sqrt

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

def process_queries(K, Q, queries):
    A = defaultdict(int)
    prime_factors_K = prime_factors(K)
    for query in queries:
        if query[0] == '!':
            _, l, r, x = query
            prime_factors_x = prime_factors(x)
            for i in range(l, r+1):
                A[i] = prime_factors_x
        else:
            _, l, r = query
            count = 0
            for i in range(l, r+1):
                if A[i] & prime_factors_K:
                    count += 1
            print(count)

K, Q = map(int, input().split())
queries = []
for _ in range(Q):
    query = input().split()
    if query[0] == '!':
        queries.append((query[0], int(query[1]), int(query[2]), int(query[3])))
    else:
        queries.append((query[0], int(query[1]), int(query[2])))
process_queries(K, Q, queries)
