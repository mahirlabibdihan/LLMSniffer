import math

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2),
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            factors.add(i),
            n = n / i
    if n > 2:
        factors.add(n)
    return len(factors)

def energy_needed(n, m):
    return sum(prime_factors(i) for i in range(n, m+1))

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(energy_needed(n, m))