T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(0)
    elif N & (N + 1) == 0:
        print(N // 2)
    else:
        print(-1)