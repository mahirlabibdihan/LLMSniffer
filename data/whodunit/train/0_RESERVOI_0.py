T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    reservoir = [list(input().strip()) for _ in range(N)]
    stable = True
    for i in range(N):
        for j in range(M):
            if reservoir[i][j] == 'W':
                if j == 0 or j == M-1 or reservoir[i][j-1] == 'A' or reservoir[i][j+1] == 'A' or (i < N-1 and reservoir[i+1][j] == 'A'):
                    stable = False
                    break
            elif reservoir[i][j] == 'B':
                if i < N-1 and reservoir[i+1][j] == 'A':
                    stable = False
                    break
        if not stable:
            break
    print("yes" if stable else "no")