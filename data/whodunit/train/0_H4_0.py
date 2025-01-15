t = int(input().strip())
mod = 10**9+7
for _ in range(t):
    n, m = map(int,input().strip().split())
    n %= mod
    m %= mod
    ans = 0
    for i in range(1, n+1):
        ans = (ans + pow(i, i, m)) % m
    print(ans)