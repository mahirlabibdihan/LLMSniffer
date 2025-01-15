def count_cells(T, test_cases):
    for t in range(T):
        N, grid = test_cases[t]
        count = 0
        for i in range(N):
            if '#' not in grid[i]:
                count += grid[i].count('.')
            else:
                count += grid[i].count('.', 0, grid[i].index('#'))
        print(count)

T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    grid = [list(input().strip()) for _ in range(N)]
    test_cases.append((N, grid))
count_cells(T, test_cases)