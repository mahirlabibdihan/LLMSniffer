def min_stones(T, test_cases):
    for i in range(T):
        N, M, K = test_cases[i]
        if K <= (N-1) + (M-1):
            print(K)
        else:
            print(max(N, M) - 1 + min(N, M) - 1 + (K - (N + M - 2)) // 2)

T = int(input())
test_cases = []
for _ in range(T):
    N, M, K = map(int, input().split())
    test_cases.append((N, M, K))
min_stones(T, test_cases)