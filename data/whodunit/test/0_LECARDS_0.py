import sys
from collections import Counter

MOD = 10**9 + 7
MAX = 10**4 + 10
fact = [0]*MAX
invfact = [0]*MAX

def add(x, y):
    return (x+y)%MOD

def mul(x, y):
    return (x*y)%MOD

def power(x, y):
    res = 1
    while y:
        if y&1:
            res = mul(res, x)
        y >>= 1
        x = mul(x, x)
    return res

def inv(x):
    return power(x, MOD-2)

def C(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return mul(fact[n], mul(invfact[r], invfact[n-r]))

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    counter = Counter(c)
    odd, even = 0, 0
    for i in counter.values():
        if i&1:
            odd += 1
        else:
            even += 1
    dp = [0]*(odd+1)
    dp[0] = power(2, even)
    for i in range(1, odd+1):
        dp[i] = add(dp[i-1], dp[i-1])
    ans = dp[odd]
    for i in range(odd+1, n+1, 2):
        ans = add(ans, mul(C(n, i), power(2, n-i)))
    print(ans)

fact[0] = 1
for i in range(1, MAX):
    fact[i] = mul(i, fact[i-1])
invfact[MAX-1] = inv(fact[MAX-1])
for i in range(MAX-2, -1, -1):
    invfact[i] = mul(invfact[i+1], i+1)

t = int(input())
for _ in range(t):
    solve()