from sys import stdin, stdout
from collections import defaultdict

def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(v, p):
    size[v] = 1
    max_c[v] = 0
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v)
        size[v] += size[u]
        max_c[v] = max(max_c[v], size[u])
    max_c[v] = max(max_c[v], n - size[v])

def solve():
    global n, graph, size, max_c
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    graph = defaultdict(list)
    size = [0] * (n + 1)
    max_c = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        add_edge(u, v)
    dfs(1, 0)
    min_c = min(max_c[1:])
    capitals = [i for i in range(1, n + 1) if max_c[i] == min_c]
    max_p = max(p[i - 1] for i in capitals)
    capital = capitals[p.index(max_p)]
    for _ in range(n):
        stdout.write(str(capital) + ' ')
    stdout.write('\n')

t = int(stdin.readline())
for _ in range(t):
    solve()