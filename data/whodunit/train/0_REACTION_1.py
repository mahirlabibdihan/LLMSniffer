T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    stable = "Stable"
    for i in range(R):
        for j in range(C):
            if (i == 0 or i == R-1) and (j == 0 or j == C-1):
                if grid[i][j] > 2:
                    stable = "Unstable"
                    break
            elif i == 0 or i == R-1 or j == 0 or j == C-1:
                if grid[i][j] > 3:
                    stable = "Unstable"
                    break
            elif grid[i][j] > 4:
                stable = "Unstable"
                break
        if stable == "Unstable":
            break
    print(stable)