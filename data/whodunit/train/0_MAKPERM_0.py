def min_moves(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        print(N - len(set([i for i in A if i <= N])))

T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, A))

min_moves(T, test_cases)