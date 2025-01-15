def max_steps(T, test_cases):
    for i in range(T):
        N, M = test_cases[i]
        print(N*M - 1)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))

max_steps(T, test_cases)