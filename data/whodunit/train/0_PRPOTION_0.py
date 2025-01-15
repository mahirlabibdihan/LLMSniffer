T = int(input())
for _ in range(T):
    R, G, B, M = map(int, input().split())
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for _ in range(M):
        max_val = max(max(r), max(g), max(b))
        if max_val == max(r):
            r = [i//2 for i in r]
        elif max_val == max(g):
            g = [i//2 for i in g]
        else:
            b = [i//2 for i in b]
    print(max(max(r), max(g), max(b)))