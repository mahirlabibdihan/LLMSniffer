T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    trips = 0
    while len(W) > 0:
        load = 0
        i = 0
        while i < len(W):
            if load + W[i] <= K:
                load += W[i]
                del W[i]
            else:
                i += 1
        if load > 0:
            trips += 1
        else:
            print(-1)
            break
    else:
        print(trips)