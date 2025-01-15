T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(N - i - 1)
    print(*B)