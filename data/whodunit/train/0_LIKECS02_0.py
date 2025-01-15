T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    elif N == 2:
        print(-1)
    else:
        arr = [i for i in range(1, N+1)]
        arr[1], arr[N-1] = arr[N-1], arr[1]
        print(' '.join(map(str, arr)))