from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def chef_conjecture(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i + j**2 + k**3 == n:
                    return i, j, k
    return 0, 0, 0

while True:
    n = int(input())
    if n == 0:
        break
    p1, p2, p3 = chef_conjecture(n)
    print(p1, p2, p3)