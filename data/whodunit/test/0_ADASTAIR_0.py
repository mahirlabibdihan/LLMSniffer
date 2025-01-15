T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    steps = 0
    for i in range(1, N):
        steps += (h[i] - h[i-1] - 1) // K
    print(steps)