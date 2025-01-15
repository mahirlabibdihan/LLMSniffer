def calculate_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    a1 = calculate_area(x1, y1, x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    a2 = calculate_area(x1, y1, x2, y2)
    print(a1 + a2)