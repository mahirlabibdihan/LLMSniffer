def is_reachable(x, y):
    x, y = abs(x), abs(y)
    if x < y:
        x, y = y, x
    if x == y:
        return x % 2 == 0
    elif x - y == 1 and x % 2 == 1:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print("YES" if is_reachable(x, y) else "NO")