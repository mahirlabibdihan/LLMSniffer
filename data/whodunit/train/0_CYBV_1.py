def min_weapons(T, test_cases):
    for i in range(T):
        N, K = test_cases[i]
        if K % N == 0:
            print(K // N)
        else:
            print(K // N)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
min_weapons(T, test_cases)