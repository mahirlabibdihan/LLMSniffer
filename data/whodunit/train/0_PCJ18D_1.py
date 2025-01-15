def min_cookies(T, test_cases):
    for i in range(T):
        N, B = test_cases[i]
        A = (N + B - 1) // B
        print(A)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))

min_cookies(T, test_cases)