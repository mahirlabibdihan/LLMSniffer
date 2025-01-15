def max_age(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    for i in range(n-1, -1, -1):
        if '0' <= s[i] <= '9':
            dp[0][i] = max(dp[0][i+1], int(s[i]) + 10*dp[1][i+1])
            dp[1][i] = max(dp[1][i+1], int(s[i]) + 10*dp[0][i+1])
        else:
            dp[1][i] = max(dp[1][i+1], 9 + 10*dp[0][i+1])
    return max(dp[0][0], dp[1][0])

s = input().strip()
print(max_age(s))