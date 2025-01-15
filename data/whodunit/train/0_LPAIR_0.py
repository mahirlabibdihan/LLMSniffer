def countIntersections(lines):
    lines.sort(key=lambda x: x[1])
    tree, cnt = [0]*800005, 0
    for i in range(len(lines)):
        u = lines[i][0]
        cnt += sum(tree[u+1:])
        v = lines[i][0]
        while v <= 100000:
            tree[v] += 1
            v += v & -v
    return cnt

N = int(input().strip())
lines = []
for _ in range(N):
    M, F = map(int, input().strip().split())
    lines.append((M, F))
print(countIntersections(lines))