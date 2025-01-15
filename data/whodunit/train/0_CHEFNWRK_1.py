T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    trips = 0
    while W:
        load = 0
        for i in reversed(range(len(W))):
            if load + W[i] <= K:
                load += W.pop(i)
        if load > 0:
            trips += 1
        else:
            print(-1)
            break
    else:
        print(trips)