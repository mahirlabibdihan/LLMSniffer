T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 2:
        print(-1)
    else:
        print(2*N)