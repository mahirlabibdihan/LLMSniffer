T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if min(A) < 2:
        print(-1)
    else:
        print(2*N)