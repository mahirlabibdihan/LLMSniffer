MOD = 10**9 + 7

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(map(int, input().split()))
        S.sort()
        ans = 0
        for i in range(N):
            ans = (ans + (S[i] * pow(2, i, MOD)) % MOD - (S[i] * pow(2, N-i-1, MOD)) % MOD) % MOD
        print(ans)

solve()