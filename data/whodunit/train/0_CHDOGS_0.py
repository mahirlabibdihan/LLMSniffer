import math
T = int(input())
for _ in range(T):
    s, v = map(int, input().split())
    time = s / (2 * v) * math.sqrt(3)
    print("{:.9f}".format(time))