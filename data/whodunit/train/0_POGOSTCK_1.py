def max_points(T, test_cases):
    for _ in range(T):
        N, K = test_cases[_][0]
        A = test_cases[_][1]
        dp = [0]*N
        dp[-1] = max(0, A[-1])
        for i in range(N-2, -1, -1):
            if i+K < N:
                dp[i] = max(A[i] + dp[i+K], dp[i+1])
            else:
                dp[i] = max(A[i], dp[i+1])
        print(dp[0])

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, K), A))
max_points(T, test_cases)