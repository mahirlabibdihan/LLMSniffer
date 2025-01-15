T = int(input())
for _ in range(T):
    N, M, K, L, R = map(int, input().split())
    cans = [list(map(int, input().split())) for _ in range(N)]
    cans.sort(key=lambda x: x[1])
    for C, P in cans:
        if C > K+1:
            temp = max(C - M, K+1)
        elif C < K-1:
            temp = min(C + M, K-1)
        else:
            temp = K
        if L <= temp <= R:
            print(P)
            break
    else:
        print(-1)