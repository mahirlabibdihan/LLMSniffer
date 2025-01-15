MOD = 10**9 + 7
MAX = 10**8 + 10
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

def modinv(n):
    return power(n, MOD-2)

def C(n, k):
    if k < 0 or k > n:
        return 0
    return (fact[n] * ((invfact[k] * invfact[n-k]) % MOD)) % MOD

fact[0] = 1
for i in range(1, MAX):
    fact[i] = (i * fact[i-1]) % MOD

invfact[MAX-1] = modinv(fact[MAX-1])
for i in range(MAX-2, -1, -1):
    invfact[i] = ((i+1) * invfact[i+1]) % MOD

T = int(input())
for _ in range(T):
    N = int(input())
    print((2 * C(2*N, N) - N + MOD) % MOD)