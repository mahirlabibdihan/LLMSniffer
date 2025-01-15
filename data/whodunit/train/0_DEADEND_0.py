T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(1, N):
        count += A[i] - A[i-1] - 1
    print(count)