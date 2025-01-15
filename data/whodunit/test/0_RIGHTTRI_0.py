import math

T = int(input())
for _ in range(T):
    H, S = map(int, input().split())
    x = (H**2 - 4*S)
    if x < 0:
        print(-1)
    else:
        a = (H + math.sqrt(x)) / 2
        b = (H - math.sqrt(x)) / 2
        print(min(a, b), max(a, b), H)