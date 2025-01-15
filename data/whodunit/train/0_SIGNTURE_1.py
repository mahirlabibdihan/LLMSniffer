def solve():
    n, m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    b = [list(map(int, list(input().strip()))) for _ in range(n)]
    ans = float('inf')
    for dx in range(-n+1, n):
        for dy in range(-m+1, m):
            cnt = 0
            for i in range(n):
                for j in range(m):
                    if i+dx < 0 or i+dx >= n or j+dy < 0 or j+dy >= m:
                        cnt += a[i][j]
                    else:
                        cnt += a[i][j] != b[i+dx][j+dy]
            ans = min(ans, cnt)
    print(ans)

t = int(input())
for _ in range(t):
    solve()
