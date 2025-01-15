T = int(input())
for _ in range(T):
    N = int(input())
    for x in range(0, N+1, 7):
        if (N - x) % 4 == 0:
            print(x)
            break
    else:
        print(-1)