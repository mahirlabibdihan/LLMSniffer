T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    grid = [list(input().strip()) for _ in range(N)]
    count = 0
    for i in range(N):
        if '#' not in grid[i]:
            count += grid[i].count('.')
        else:
            count += grid[i].count('.', 0, grid[i].index('#'))
    print(count)