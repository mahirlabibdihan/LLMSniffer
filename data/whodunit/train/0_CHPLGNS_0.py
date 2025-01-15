from operator import itemgetter

def solve():
    n = int(input())
    polygons = []
    for _ in range(n):
        m = int(input())
        points = list(map(int, input().split()))
        min_point = min((points[i], points[i + 1]) for i in range(0, len(points), 2))
        polygons.append((min_point, m - 1))
    polygons.sort(key=itemgetter(0))
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