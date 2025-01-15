def max_tastiness(T, test_cases):
    for _ in range(T):
        N, M, dishes = test_cases[_]
        days = [0]*(M+1)
        for i in range(N):
            D, V = dishes[i]
            days[D] = max(days[D], V)
        max1 = max(days)
        days.remove(max1)
        max2 = max(days)
        print(max1 + max2)

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    dishes = [list(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, M, dishes))
max_tastiness(T, test_cases)