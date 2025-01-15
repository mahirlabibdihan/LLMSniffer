from sys import stdin, stdout
from collections import deque
mod = 10**9+7

def solve():
    n = int(stdin.readline())
    grid = [list(stdin.readline().strip()) for _ in range(n)]
    row = [0]*n
    col = [0]*n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                row[i] = j
                col[j] = i
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i:
                dp[i][j] = dp[i-1][j]
            if j:
                dp[i][j] = (dp[i][j] + dp[i][j-1])%mod
            if i and j and row[i-1] <= j-1 and col[j-1] <= i-1:
                dp[i][j] = (dp[i][j] - dp[i-1][j-1] + mod)%mod
    stdout.write(str(dp[n-1][n-1])+'\n')

t = int(stdin.readline())
for _ in range(t):
    solve()