def min_sum(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        print(sum(A) - 2*min(A))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

min_sum(T, test_cases)