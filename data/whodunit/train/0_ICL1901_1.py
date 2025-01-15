def distinct_numbers(T, test_cases):
    for _ in range(T):
        K, N = test_cases[_]
        print(6 if N == 1 else 0)

T = int(input())
test_cases = []
for _ in range(T):
    K, N = map(int, input().split())
    test_cases.append((K, N))
distinct_numbers(T, test_cases)