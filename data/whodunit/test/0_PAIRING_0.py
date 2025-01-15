def max_pairing(n, m, pairs):
    used = [False]*n
    pairs.sort(key=lambda x: x[2], reverse=True)
    result = []
    for i in range(m):
        if not used[pairs[i][0]] and not used[pairs[i][1]]:
            used[pairs[i][0]] = used[pairs[i][1]] = True
            result.append(pairs[i][2])
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