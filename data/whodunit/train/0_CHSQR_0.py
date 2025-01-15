T = int(input())
for _ in range(T):
    K = int(input())
    grid = [[0]*K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            if (i+j)%2 == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = 2
    for row in grid:
        print(*row)