T = int(input())
for _ in range(T):
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    print(max(heights))