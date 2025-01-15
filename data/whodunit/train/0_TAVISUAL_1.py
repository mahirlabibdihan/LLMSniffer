def find_ball(T, test_cases):
    for i in range(T):
        N, C, Q, operations = test_cases[i]
        for j in range(Q):
            L, R = operations[j]
            if L <= C <= R:
                C = L + R - C
        print(C)

T = int(input())
test_cases = []
for _ in range(T):
    N, C, Q = map(int, input().split())
    operations = [list(map(int, input().split())) for _ in range(Q)]
    test_cases.append((N, C, Q, operations))

find_ball(T, test_cases)