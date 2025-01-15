MOD = 10**9 + 7
MAX = 10**4 + 10
fact = [1]*MAX
invfact = [1]*MAX

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

for i in range(1, MAX):
    fact[i] = mul(i, fact[i-1])
invfact[MAX-1] = inv(fact[MAX-1])
for i in range(MAX-2, -1, -1):
    invfact[i] = mul(invfact[i+1], i+1)

t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    counter = [0]*1001
    for i in c:
        counter[i] += 1
    odd, even = 0, 0
    for i in counter:
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