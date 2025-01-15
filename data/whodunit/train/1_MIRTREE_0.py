mod = 1000000007
n, q = map(int, input().split())
height = n
depth = n + 1
topwidth = 1
width = pow(2, n, mod)
edges = (pow(2, depth, mod) + mod - 2) % mod
for _ in range(q):
    act = tuple(map(int, input().split()))
    if act[0] == 2:
        print(edges)
    else:
        if act[1] <= 2: # left or right
            edges = ((2 * edges) % mod + depth) % mod
            topwidth = (topwidth * 2) % mod
            width = (width * 2) % mod
        elif act[1] == 3: # top
            edges = ((2 * edges) % mod + topwidth) % mod
            topwidth = width
            depth = (depth * 2) % mod
        else: # bottom
            edges = ((2 * edges) % mod + width) % mod
            width = topwidth
            depth = (depth * 2) % mod
