def solve(N, K):
    if K % 2 == 0:
        return [K] * N
    else:
        return [K - 1] * (N - 1) + [K]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(' '.join(map(str, solve(N, K))))