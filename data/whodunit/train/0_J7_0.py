import math

t = int(input())
for _ in range(t):
    P, S = map(int, input().split())
    a = (P - math.sqrt(P**2 - 24*S)) / 12
    volume = a * (S/2 - a * P/4)
    print("{:.2f}".format(volume))