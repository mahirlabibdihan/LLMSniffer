def max_trace(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        trace = [0]*(N+1)
        for i in range(N, 0, -1):
            for j in range(N, 0, -1):
                trace[min(i, j)] = max(trace[min(i, j)], A[i-1][j-1] + trace[min(i+1, j+1) - 1])
        print(max(trace))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, A))
max_trace(T, test_cases)