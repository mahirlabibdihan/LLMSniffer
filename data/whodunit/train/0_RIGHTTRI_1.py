import math

def solve(H, S):
    x = H**2 - 4*S
    if x < 0:
        return -1
    else:
        a = (H + math.sqrt(x)) / 2
        b = (H - math.sqrt(x)) / 2
        return min(a, b), max(a, b), H

T = int(input())
for _ in range(T):
    H, S = map(int, input().split())
    result = solve(H, S)
    if result == -1:
        print(-1)
    else:
        print(*result)