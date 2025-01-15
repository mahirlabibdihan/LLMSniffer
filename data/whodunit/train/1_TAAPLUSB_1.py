dp = [0] * 100000
dp[0] = 0.45
for i in range(1, 100000):
    dp[i] = dp[i - 1] + 0.5 - (5 * pow(10, -(i + 2)))
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    print('{0:.6f}\n'.format(dp[n - 1]))