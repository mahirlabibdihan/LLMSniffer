T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    x, y = abs(x), abs(y)
    if x < y:
        x, y = y, x
    if x > y * 2:
        print(x * 2)
    elif x % 2 == y % 2:
        print(x * 2)
    else:
        print(x * 2 - 1)