def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

N = int(input())
areas = []
for i in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    areas.append(calculate_area(x1, y1, x2, y2, x3, y3))

min_area = min(areas)
max_area = max(areas)

print(areas.index(min_area) + 1, areas.index(max_area) + 1)