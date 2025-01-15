MOD = 10**9 + 7
MAX = 10**6 + 5
fact = [0]*MAX
invfact = [0]*MAX

def power(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res

def inv(n):
    return power(n, MOD - 2)

def C(n, k):
    if k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n - k]) % MOD

def solve(n):
    return (2 * C(2*n - 1, n - 1)) % MOD

fact[0] = 1
for i in range(1, MAX):
    fact[i] = (i * fact[i - 1]) % MOD

invfact[MAX - 1] = inv(fact[MAX - 1])
for i in range(MAX - 2, -1, -1):
    invfact[i] = ((i + 1) * invfact[i + 1]) % MOD

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
