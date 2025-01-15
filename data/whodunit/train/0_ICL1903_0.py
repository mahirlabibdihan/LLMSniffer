T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
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