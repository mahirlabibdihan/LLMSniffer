def distinct_colors(T, test_cases):
    for _ in range(T):
        N, M, heights, colors = test_cases[_]
        heights, colors = zip(*sorted(zip(heights, colors), reverse=True))
        distinct_colors = set()
        distinct_colors.add(colors[0])
        for i in range(1, N):
            if heights[i] != heights[i-1]:
                distinct_colors.add(colors[i])
        print(len(distinct_colors))

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    test_cases.append((N, M, heights, colors))
distinct_colors(T, test_cases)