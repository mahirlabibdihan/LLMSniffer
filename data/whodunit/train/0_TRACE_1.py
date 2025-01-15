def max_trace(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(N, 0, -1):
            for j in range(N, 0, -1):
                dp[i][j] = A[i-1][j-1] + dp[i+1][j+1]
        print(max(max(row) for row in dp))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, A))
max_trace(T, test_cases)