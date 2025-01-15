def check(i, n, height):
    for j in range(i  + 1, n):
        if height[j] >= height[i]:
            return False
    return True
T = int(input())
for _ in range(T):
    n, c = map(int, input().split())
    height = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    distinct_colors = []
    for i in range(n - 1):
        if check(i, n, height) and colors[i] not in distinct_colors:
            distinct_colors.append(colors[i])
    if colors[n -1] not in distinct_colors:
        distinct_colors.append(colors[n - 1])
    print(len(distinct_colors))