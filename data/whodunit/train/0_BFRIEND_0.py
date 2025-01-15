T = int(input())
for _ in range(T):
    N, a, b, c = map(int, input().split())
    F = list(map(int, input().split()))
    min_time = float('inf')
    for i in range(N):
        time = abs(F[i] - b) + abs(a - F[i]) + c
        if time < min_time:
            min_time = time
    print(min_time)