T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K % 2 == 0:
        print(' '.join([str(K)] * N))
    else:
        print(' '.join([str(K - 1)] * (N - 1) + [str(K)]))