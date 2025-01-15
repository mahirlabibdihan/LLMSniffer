T = int(input())
for _ in range(T):
    R, G, B = map(int, input().split())
    K = int(input())
    min_balloons = min(R, G, B, K-1)
    print(min_balloons*3 + 1)