MOD = 10**9 + 7
MAX = 10**9 + 7

def solve():
    dp = [0]*(MAX+1)
    dp[0] = dp[1] = 1
    for i in range(2, MAX+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp[N])

solve()