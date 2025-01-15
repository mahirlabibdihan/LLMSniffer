T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[i]*P[0] for i in range(1, N)))