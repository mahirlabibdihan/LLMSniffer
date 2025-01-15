T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    while X != Y and X != 0 and Y != 0:
        if X > Y:
            X -= Y
        else:
            Y -= X
    print(X + Y)