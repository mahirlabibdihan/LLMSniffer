def is_CPC(grid, j , k):
    l = k-1
    L = 0
    while(l >= 0):
        if grid[j][l] == '^':
            L = L + 1
        else:
            break
        l = l - 1
    if L < 2:
        return False
    l = k+1
    R = 0
    while(l < n):
        if grid[j][l] == '^':
            R = R + 1
        else:
            break
        l = l+1
    if R < 2:
        return False
    l = j-1
    T = 0
    while(l >= 0):
        if grid[l][k] == '^':
            T = T+1
        else:
            break
        l = l-1
    if T < 2:
        return False
    l = j+1
    B = 0
    while(l < m):
        if grid[l][k] == '^':
            B = B + 1
        else:
            break
        l = l+1
    if B < 2:
        return False
    return True


T = int(input())
for i in range(T):
    m,n = input().split()
    m = int(m)
    n = int(n)
    grid = []
    for j in range(m):
        row = str(input())
        grid.append(row)
    monsters = 0
    for j in range(m):
        for k in range(n):
            if grid[j][k] == '^' and is_CPC(grid, j, k):
                monsters = monsters + 1
    print(monsters)