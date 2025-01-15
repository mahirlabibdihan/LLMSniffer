T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    x, y = abs(x), abs(y)
    if x < y:
        x, y = y, x
    if x == y:
        print("YES" if x % 2 == 0 else "NO")
    elif x - y == 1 and x % 2 == 1:
        print("YES")
    else:
        print("NO")