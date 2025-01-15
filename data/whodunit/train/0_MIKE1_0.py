def solve():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    l = int(input())
    pairs = [list(map(int, input().split())) for _ in range(l)]
    e1, e2 = 0, 0
    for i, j in pairs:
        i -= 1
        j -= 1
        if i < n and j < m:
            e1 += matrix[i][j]
        else:
            e1 = -1
        if j < n and i < m:
            e2 += matrix[j][i]
        else:
            e2 = -1
        if e1 == -1 and e2 == -1:
            return -1
    return max(e1, e2)

print(solve())