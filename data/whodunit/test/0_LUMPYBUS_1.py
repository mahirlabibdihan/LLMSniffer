from collections import defaultdict
def max_creatures(T, test_cases):
    for _ in range(T):
        N, P, Q = test_cases[_][0]
        A = test_cases[_][1]
        extra = defaultdict(int)
        for i in A:
            extra[i%2] += 1
        Q = min(Q, extra[0])
        P = min(P, extra[1] - extra[1]%2)
        if P < extra[1]:
            Q = min(Q-1, extra[0])
        print(Q + P)

T = int(input())
test_cases = []
for _ in range(T):
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, P, Q), A))
max_creatures(T, test_cases)