def solve():
    N, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*K for _ in range(N)]
    dp[0] = [x/sum(a[0]) for x in a[0]]
    for i in range(1, N):
        total = sum(a[i])
        for j in range(K):
            dp[i][j] = sum(dp[i-1][k] * a[i][j] / total for k in range(K))
            total -= a[i][j]
    print(*dp[-1])

solve()