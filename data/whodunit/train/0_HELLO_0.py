T = int(input())
for _ in range(T):
    D, U, N = map(float, input().split())
    N = int(N)
    plans = []
    for i in range(N):
        M, R, C = map(float, input().split())
        M = int(M)
        C = int(C)
        plans.append((C/M + R*U, i+1))
    plans.sort()
    if D*U <= plans[0][0]:
        print(0)
    else:
        print(plans[0][1])