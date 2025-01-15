def max_profit(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        B = test_cases[_][2]
        max_profit = 0
        for i in range(N):
            if A[i] > B[i]:
                if A[i] > max_profit:
                    max_profit = A[i]
            else:
                if B[i] > max_profit:
                    max_profit = B[i]
        print(max_profit)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append((N, A, B))
max_profit(T, test_cases)