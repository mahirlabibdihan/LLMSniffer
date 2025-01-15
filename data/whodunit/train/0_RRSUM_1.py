N, M = map(int, input().split())
queries = [int(input()) for _ in range(M)]
for q in queries:
    if q <= N + 1:
        print(max(0, q - 1 - N))
    elif q > 2 * N:
        print(0)
    else:
        print(N - (q - N - 1))