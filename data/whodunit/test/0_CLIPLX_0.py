T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(max(0, (X - Y + 1) // 2))