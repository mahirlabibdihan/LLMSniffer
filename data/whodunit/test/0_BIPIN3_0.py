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
    if k < 0 or n < k:
        return 0
    return (fact[n] * ((invfact[k] * invfact[n - k]) % MOD)) % MOD

def add(x, y):
    res = x + y
    if res >= MOD:
        return res - MOD
    return res

def mul(x, y):
    return (x * y) % MOD

def init():
    fact[0] = 1
    invfact[0] = 1
    for i in range(1, MAX):
        fact[i] = mul(fact[i - 1], i)
        invfact[i] = inv(fact[i])

def solve():
    init()
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        dp = [0]*(N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            dp[i] = mul(C(K, i), dp[i - 1])
            if i > 1:
                dp[i] = add(dp[i], mul(mul(C(K, i), dp[i - 2]), mul(i - 1, i)))
        print(dp[N])
solve()