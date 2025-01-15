T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if (b - a) % (c + d) == 0:
        print("YES")
    else:
        print("NO")