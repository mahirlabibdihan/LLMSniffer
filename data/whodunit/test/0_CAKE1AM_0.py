T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    a1 = (x2 - x1) * (y2 - y1)
    x1, y1, x2, y2 = map(int, input().split())
    a2 = (x2 - x1) * (y2 - y1)
    print(a1 + a2)