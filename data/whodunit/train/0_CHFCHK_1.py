def longest_jump(T, test_cases):
    for i in range(T):
        N = test_cases[i][0]
        a = test_cases[i][1]
        print(min(a))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    test_cases.append((N, a))

longest_jump(T, test_cases)