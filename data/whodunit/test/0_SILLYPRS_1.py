def max_sum_of_heights(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = sorted(test_cases[_][1])
        B = sorted(test_cases[_][2])
        sum_heights = 0
        for i in range(N):
            sum_heights += min(A[i], B[i])
        print(sum_heights)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append((N, A, B))

max_sum_of_heights(T, test_cases)