N, M = map(int, input().split())
for _ in range(M):
    q = int(input())
    if q <= N + 1:
        print(max(0, q - 1 - N))
    elif q > 2 * N:
        print(0)
    else:
        print(N - (q - N - 1))