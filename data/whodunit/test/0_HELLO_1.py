T = int(input())
for _ in range(T):
    D, U, N = map(float, input().split())
    N = int(N)
    min_cost = D * U
    min_plan = 0
    for i in range(N):
        M, R, C = map(float, input().split())
        M = int(M)
        C = int(C)
        cost = C/M + R*U
        if cost < min_cost:
            min_cost = cost
            min_plan = i+1
    print(min_plan)