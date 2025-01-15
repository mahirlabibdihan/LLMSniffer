import math

def max_volume(P, S):
    a = (P - math.sqrt(P**2 - 24*S)) / 12
    return a * (S/2 - a * P/4)

t = int(input())
for _ in range(t):
    P, S = map(int, input().split())
    print("{:.2f}".format(max_volume(P, S)))