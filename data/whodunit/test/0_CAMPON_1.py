def solve():
    D = int(input())
    dp = [0]*32
    for _ in range(D):
        d, p = map(int, input().split())
        dp[d] = p
    for i in range(1, 32):
        dp[i] += dp[i-1]
    Q = int(input())
    for _ in range(Q):
        dead, req = map(int, input().split())
        if dp[dead] >= req:
            print("Go Camp")
        else:
            print("Go Sleep")

T = int(input())
for _ in range(T):
    solve()