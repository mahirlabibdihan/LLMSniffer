import math

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

T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().strip().split())
    factors = prime_factors(B)
    if all(A % factor == 0 for factor in factors):
        print("Yes")
    else:
        print("No")