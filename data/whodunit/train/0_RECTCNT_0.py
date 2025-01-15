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

        rectangles = 0
        for count in points.values():
            rectangles += count * (count - 1) // 2

        print(rectangles)

count_rectangles()