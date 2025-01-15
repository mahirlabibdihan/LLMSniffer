T = int(input())
for _ in range(T):
    N, C, Q = map(int, input().split())
    for _ in range(Q):
        L, R = map(int, input().split())
        if L <= C <= R:
            C = L + R - C
    print(C)