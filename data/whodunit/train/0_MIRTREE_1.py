mod = 10**9+7
n, q = map(int,input().split())
edges = [0, 2**n-1, 2**n-1, 2**(n+1)-1, 2**(n+1)-1]
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        edges[query[1]] = (edges[query[1]]*2) % mod
    elif query[0] == 2:
        print(sum(edges) % mod)