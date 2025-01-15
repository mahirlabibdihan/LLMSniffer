MOD = 10**9+7
MAX = 305
dp = [[0]*MAX for _ in range(MAX)]
dp[0][0] = 1
for i in range(1, MAX):
    dp[i][0] = 1
    for j in range(1, min(i+1, MAX)):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD

def solve():
    n, w = map(int, input().split())
    if w < 0 or w > 9:
        return 0
    n -= 2
    ans = 0
    for i in range(w, 10):
        ans = (ans + dp[n+i-1][i-1]) % MOD
    return ans

t = int(input())
results = [solve() for _ in range(t)]
for result in results:
    print(result)