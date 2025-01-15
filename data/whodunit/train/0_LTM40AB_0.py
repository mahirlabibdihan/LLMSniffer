T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if b < c or d < a:
        print(0)
    else:
        print(min(b, d) - max(a, c) + 1)