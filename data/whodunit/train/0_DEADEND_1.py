def min_trees(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = sorted(test_cases[_][1])
        count = 0
        for i in range(1, N):
            count += A[i] - A[i-1] - 1
        print(count)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))
min_trees(T, test_cases)