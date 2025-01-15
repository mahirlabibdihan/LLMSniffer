def countIntersections(lines):
    lines.sort(key=lambda x: x[1])
    bit, cnt = [0]*(len(lines)+1), 0
    for i in range(len(lines)):
        u = lines[i][0]
        cnt += sum(bit[u+1:])
        v = lines[i][0]
        while v <= 100000:
            bit[v] += 1
            v += v & -v
    return cnt

N = int(input().strip())
lines = []
for _ in range(N):
    M, F = map(int, input().strip().split())
    lines.append((M, F))
print(countIntersections(lines))