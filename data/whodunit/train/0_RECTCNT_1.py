from collections import defaultdict

def count_rectangles():
    while True:
        n = int(input())
        if n == 0:
            break

        points = defaultdict(int)
        for _ in range(n):
            x, y = map(int, input().split())
            points[x] += 1

        rectangles = sum(count * (count - 1) // 2 for count in points.values())

        print(rectangles)

count_rectangles()