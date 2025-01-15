T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    x, y = abs(x), abs(y)
    if x == y:
        print(2 * x)
    elif x > y:
        print(2 * y + ((x - y) * 2 - 1 if (x - y) % 2 else 0))
    else:
        print(2 * x + ((y - x) * 2 - 1 if (y - x) % 2 else 0))