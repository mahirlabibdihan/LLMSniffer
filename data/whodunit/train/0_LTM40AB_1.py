def solve(a, b, c, d):
    if b < c or d < a:
        return 0
    else:
        return min(b, d) - max(a, c) + 1

T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    print(solve(a, b, c, d))