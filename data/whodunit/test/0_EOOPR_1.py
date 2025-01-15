def min_rounds(X, Y):
    if X >= Y:
        return (X - Y + 1) // 2
    else:
        return (Y - X + 1) // 2

T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(min_rounds(X, Y))