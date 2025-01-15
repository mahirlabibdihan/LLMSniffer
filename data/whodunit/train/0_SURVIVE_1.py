T = int(input())
for _ in range(T):
    N, K, S = map(int, input().split())
    if K * S <= N * S - (S // 7) * N:
        print((K * S + N - 1) // N)
    else:
        print(-1)