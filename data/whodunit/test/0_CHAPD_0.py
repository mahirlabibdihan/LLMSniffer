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
    for factor in factors:
        if A % factor != 0:
            print("No")
            break
    else:
        print("Yes")