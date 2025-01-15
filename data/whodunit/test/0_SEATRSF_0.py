MOD = 10**9 + 7
T = int(input())
for _ in range(T):
    n, m, qr, k = map(int, input().split())
    ans = pow(m, n, MOD)
    ans = (ans - pow(qr, n, MOD) + MOD) % MOD
    print(ans)