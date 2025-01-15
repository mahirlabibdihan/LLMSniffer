T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    if max(X, Y, Z) != sum([X, Y, Z]) - max(X, Y, Z):
        print("no")
    else:
        print("yes")