def max_profit(T, test_cases):
    for _ in range(T):
        A, B, C = test_cases[_]
        count = 0
        while A * 100 + B >= C:
            if B < C:
                A -= 1
                B += 100
            B -= C
            A, B = B, A
            count += 1
        print(count)

T = int(input())
test_cases = []
for _ in range(T):
    A, B, C = map(int, input().split())
    test_cases.append((A, B, C))
max_profit(T, test_cases)