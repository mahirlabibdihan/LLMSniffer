T = int(input())
for _ in range(T):
    R, G, B, M = map(int, input().split())
    r = max(map(int, input().split()))
    g = max(map(int, input().split()))
    b = max(map(int, input().split()))
    for _ in range(M):
        max_val = max(r, g, b)
        if max_val == r:
            r = r//2
        elif max_val == g:
            g = g//2
        else:
            b = b//2
    print(max(r, g, b))