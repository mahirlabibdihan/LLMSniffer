from functools import reduce


def binom(n, k, mod=10**9+7):
    
    def mul_mod(x, y):
        return (x * y) % mod
    
    if k in (0, n):
        return 1
    
    if k > n // 2:
        count = reduce(mul_mod, range(k+1, n+1))
        denom = pow(reduce(mul_mod, range(1, n-k+1)), mod-2, mod)
    else: 
        count = reduce(mul_mod, range(n-k+1, n+1))
        denom = pow(reduce(mul_mod, range(1, k+1)), mod-2, mod)
    return mul_mod(count, denom)


mod=10**9+7
for _ in range(int(input())):
    n = int(input())
    deck = input()
    
    if n % 2 == 1:
        result = pow(2, n-1, mod)
    else:
        result = (pow(2, n-1, mod) - (binom(n, n//2, mod) * ((mod + 1) // 2)) % mod) % mod
        
    print(result)
    