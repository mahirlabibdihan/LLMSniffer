def max_sum(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        C = test_cases[_][1]
        W = test_cases[_][2]
        last_occurrence = [-1]*1000005
        dp = [0]*1000005
        dp[0] = W[0]
        last_occurrence[C[0]] = 0
        for i in range(1, N):
            dp[i] = W[i] + dp[i-1]
            if last_occurrence[C[i]] != -1:
                dp[i] = min(dp[i], dp[last_occurrence[C[i]]] + W[i])
            if i != 1:
                dp[i] = max(dp[i], dp[i-1])
            last_occurrence[C[i]] = i
        print(max(dp[:N]))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    W = list(map(int, input().split()))
    test_cases.append((N, C, W))
max_sum(T, test_cases)