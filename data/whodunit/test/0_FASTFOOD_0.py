def max_profit(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        B = test_cases[_][2]
        max_profit = max(A)
        max_profit_index = A.index(max_profit)
        if max_profit < B[max_profit_index]:
            max_profit = B[max_profit_index]
        print(max_profit)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append((N, A, B))
max_profit(T, test_cases)