def min_plates(T, test_cases):
    for _ in range(T):
        N, M, P = test_cases[_]
        P.sort(reverse=True)
        count = 0
        for i in P:
            if M <= 0:
                break
            M -= i
            count += 1
        if M > 0:
            print(-1)
        else:
            print(count)

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    test_cases.append((N, M, P))
min_plates(T, test_cases)