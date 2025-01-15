def distribute_candies(T, test_cases):
    for i in range(T):
        N, M, K = test_cases[i]
        if N < M:
            print(-1)
        else:
            remainder = N % M
            if remainder == 0:
                print(0)
            elif remainder <= K:
                print(1)
            else:
                print(-1)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
distribute_candies(T, test_cases)