def max_weight(T, test_cases):
    for _ in range(T):
        n, k, oranges = test_cases[_]
        oranges.sort()
        weight = 0
        for cost, wt in oranges:
            if cost <= k:
                k -= cost
                weight += wt
        print(weight)

T = int(input())
test_cases = []
for _ in range(T):
    n, k = map(int, input().split())
    oranges = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, k, oranges))
max_weight(T, test_cases)