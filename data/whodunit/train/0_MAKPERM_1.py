def min_moves(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        unique_nums = set()
        for i in A:
            if i <= N:
                unique_nums.add(i)
        print(N - len(unique_nums))

T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, A))

min_moves(T, test_cases)