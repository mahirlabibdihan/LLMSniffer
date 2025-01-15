import collections

n = int(input())
while n != 0:
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    points.sort()
    
    ans = 0
    sides = collections.defaultdict(int)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if x1 == x2:
            ans += sides[y1, y2]
            sides[y1, y2] += 1
    print(ans)
    
    n = int(input())
    