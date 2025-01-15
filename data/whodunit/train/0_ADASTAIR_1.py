def min_steps(T, test_cases):
    for _ in range(T):
        N, K, h = test_cases[_]
        steps = 0
        for i in range(1, N):
            steps += (h[i] - h[i-1] - 1) // K
        print(steps)

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    test_cases.append((N, K, h))
min_steps(T, test_cases)