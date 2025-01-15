MOD = 10**9 + 7
def solve(n, m, qr, k):
    return (pow(m, n, MOD) - pow(qr, n, MOD) + MOD) % MOD

T = int(input())
for _ in range(T):
    n, m, qr, k = map(int, input().split())
    print(solve(n, m, qr, k))