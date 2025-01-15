def max_pairing(n, m, pairs):
    used = [0]*n
    pairs = sorted(pairs, key=lambda x: x[2], reverse=True)
    result = []
    for u, v, i in pairs:
        if not used[u] and not used[v]:
            used[u] = used[v] = 1
            result.append(i)
    result.sort()
    return result

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    pairs = []
    for i in range(m):
        u, v = map(int, input().strip().split())
        pairs.append((u, v, i))
    result = max_pairing(n, m, pairs)
    print(' '.join(map(str, result)))