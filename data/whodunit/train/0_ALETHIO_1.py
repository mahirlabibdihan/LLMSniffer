def max_age(s):
    n = len(s)
    dp = [0]*(n+1)
    dp1 = [0]*(n+1)
    for i in range(n-1, -1, -1):
        if '0' <= s[i] <= '9':
            dp[i] = max(dp[i+1], int(s[i]) + 10*dp1[i+1])
            dp1[i] = max(dp1[i+1], int(s[i]) + 10*dp[i+1])
        else:
            dp1[i] = max(dp1[i+1], 9 + 10*dp[i+1])
    return max(dp[0], dp1[0])

s = input().strip()
print(max_age(s))