def distinct_colors(T, test_cases):
    for _ in range(T):
        N, M, heights, colors = test_cases[_]
        heights_colors = sorted([(heights[i], colors[i]) for i in range(N)], reverse=True)
        distinct_colors = [heights_colors[0][1]]
        for i in range(1, N):
            if heights_colors[i][0] != heights_colors[i-1][0]:
                distinct_colors.append(heights_colors[i][1])
        print(len(set(distinct_colors)))

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    test_cases.append((N, M, heights, colors))
distinct_colors(T, test_cases)