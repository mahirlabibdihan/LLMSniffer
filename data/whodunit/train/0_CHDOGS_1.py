from math import sqrt
T = int(input())
for _ in range(T):
    s, v = map(int, input().split())
    time = (s * sqrt(3)) / (2 * v)
    print("%.9f" % time)