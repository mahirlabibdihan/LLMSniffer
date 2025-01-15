T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = [N - i - 1 for i in range(N)]
    print(*B)