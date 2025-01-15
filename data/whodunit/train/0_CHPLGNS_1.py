def solve():
    n = int(input())
    polygons = []
    for i in range(n):
        m = int(input())
        points = list(map(int, input().split()))
        min_point = min((points[j], points[j + 1]) for j in range(0, len(points), 2))
        polygons.append((min_point, i))
    polygons.sort()
    ans = [0] * n
    j = 0
    for i in range(1, n):
        while polygons[j][0] < polygons[i][0]:
            j += 1
        ans[polygons[i][1]] = j
    print(*ans)

t = int(input())
for _ in range(t):
    solve()