def greet_guests(n):
    MOD = 10**9 + 7
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(greet_guests(N))