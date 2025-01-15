TC = int(input())
for _ in range(TC):
    N, K = map(int, input().split())
    total_cost = 0
    total_time = 0
    for _ in range(N):
        T, D = map(int, input().split())
        if total_time < K:
            if total_time + T <= K:
                total_time += T
            else:
                total_cost += D * (T - (K - total_time))
                total_time = K
        else:
            total_cost += D * T
    print(total_cost)