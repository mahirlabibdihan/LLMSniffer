import math
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(math.ceil(max(0, (X - Y) / 2)))