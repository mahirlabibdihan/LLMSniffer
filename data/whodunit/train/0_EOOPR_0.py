T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if X >= Y:
        print((X - Y + 1) // 2)
    else:
        print((Y - X + 1) // 2)