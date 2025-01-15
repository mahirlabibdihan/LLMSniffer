def max_profit(T, test_cases):
    for _ in range(T):
        A, B, C = test_cases[_]
        count = 0
        while True:
            if B < C and A > 0:
                A -= 1
                B += 100
            elif B >= C:
                B -= C
                A, B = B, A
                count += 1
            else:
                break
        print(count)

T = int(input())
test_cases = []
for _ in range(T):
    A, B, C = map(int, input().split())
    test_cases.append((A, B, C))
max_profit(T, test_cases)