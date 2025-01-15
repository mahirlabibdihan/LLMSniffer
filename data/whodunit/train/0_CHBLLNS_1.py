def min_balloons(T, test_cases):
    for _ in range(T):
        R, G, B, K = test_cases[_]
        min_balloons = min(R, G, B, K-1)
        print(min_balloons*3 + 1)

T = int(input())
test_cases = []
for _ in range(T):
    R, G, B = map(int, input().split())
    K = int(input())
    test_cases.append((R, G, B, K))
min_balloons(T, test_cases)