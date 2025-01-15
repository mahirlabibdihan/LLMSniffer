MOD = 10**9+7
N = 10**6
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, 8):
    for j in range(i, N+1):
        dp[j] = (dp[j] + dp[j-i]) % MOD
for i in range(7, 0, -1):
    for j in range(N, i-1, -1):
        dp[j] = (dp[j] + dp[j-i]) % MOD
dp[0] = 0
for i in range(1, N+1):
    dp[i] = (dp[i] + dp[i-1]) % MOD
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])