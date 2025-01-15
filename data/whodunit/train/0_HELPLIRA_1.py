def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

N = int(input())
areas = []
for i in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    areas.append(calculate_area(x1, y1, x2, y2, x3, y3))

min_area = max_area = areas[0]
min_index = max_index = 1

for i in range(1, N):
    if areas[i] <= min_area:
        min_area = areas[i]
        min_index = i + 1
    if areas[i] >= max_area:
        max_area = areas[i]
        max_index = i + 1

print(min_index, max_index)