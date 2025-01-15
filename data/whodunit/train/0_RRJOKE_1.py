def solve():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y, i + 1))
    points.sort()
    ans = [points[0][2]]
    points.pop(0)
    while points:
        next_point = min(points, key=lambda p: min(abs(p[0] - ans[-1][0]), abs(p[1] - ans[-1][1])))
        ans.append(next_point[2])
        points.remove(next_point)
    print(reduce(lambda x, y: x ^ y, ans))

t = int(input())
for _ in range(t):
    solve()