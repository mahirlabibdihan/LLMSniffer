MOD = 10**9+7
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[-1]
    for i in range(n-1, 0, -1):
        ans = (ans*2 % MOD + a[i-1]) % MOD
    print(ans)

t = int(input())
for _ in range(t):
    solve()