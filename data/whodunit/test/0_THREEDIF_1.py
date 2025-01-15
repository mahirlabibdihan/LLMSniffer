def solve(n1, n2, n3):
    MOD = 10**9 + 7
    n1 %= MOD
    n2 %= MOD
    n3 %= MOD
    ans = (n1 * n2 * n3) % MOD
    ans = (ans - (n1 * n2 + n2 * n3 + n3 * n1) % MOD + MOD) % MOD
    ans = (ans + (n1 + n2 + n3) % MOD) % MOD
    ans = (ans - 1 + MOD) % MOD
    return ans

T = int(input().strip())
for _ in range(T):
    n1, n2, n3 = map(int, input().strip().split())
    print(solve(n1, n2, n3))