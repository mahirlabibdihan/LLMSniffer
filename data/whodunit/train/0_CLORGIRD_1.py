T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(N)]
    possible = True
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                if i < N-1 and j < M-1 and grid[i+1][j] == '.' and grid[i][j+1] == '.' and grid[i+1][j+1] == '.':
                    grid[i][j] = '#'
                    grid[i+1][j] = '#'
                    grid[i][j+1] = '#'
                    grid[i+1][j+1] = '#'
                else:
                    possible = False
                    break
        if not possible:
            break
    if possible:
        print("YES")
    else:
        print("NO")