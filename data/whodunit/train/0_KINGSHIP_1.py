T = int(input())
for _ in range(T):
    N = int(input())
    P = sorted(map(int, input().split()))
    print(sum(P[i]*P[0] for i in range(1, N)))