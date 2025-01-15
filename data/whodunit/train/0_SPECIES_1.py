MOD = 10**9+7
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
 
def add(x, y):
    return (x+y)%MOD
 
def mul(x, y):
    return (x*y)%MOD
 
def dfs(x, y, c):
    if x<0 or x>=n or y<0 or y>=n:
        return 1
    if grid[x][y] != '?':
        if grid[x][y] != c:
            return 0
        if dp[x][y][c] != -1:
            return dp[x][y][c]
        ans = 0
        for i in range(4):
            ans = add(ans, dfs(x+dx[i], y+dy[i], c))
        dp[x][y][c] = ans
        return ans
    if dp[x][y][c] != -1:
        return dp[x][y][c]
    ans = 0
    for i in range(3):
        if c == i:
            continue
        ans = add(ans, dfs(x+dx[0], y+dy[0], i))
    dp[x][y][c] = ans
    return ans
 
t = int(input().strip())
while t > 0:
    n = int(input().strip())
    grid = [list(input().strip()) for _ in range(n)]
    dp = [[[-1]*3 for _ in range(n)] for _ in range(n)]
    ans = 0
    for i in range(3):
        ans = add(ans, dfs(0, 0, i))
    print(ans)
    t -= 1