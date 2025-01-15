def is_stable(reservoir, N, M):
    for i in range(N):
        for j in range(M):
            if reservoir[i][j] == 'W':
                if j == 0 or j == M-1 or reservoir[i][j-1] == 'A' or reservoir[i][j+1] == 'A' or (i < N-1 and reservoir[i+1][j] == 'A'):
                    return False
            elif reservoir[i][j] == 'B':
                if i < N-1 and reservoir[i+1][j] == 'A':
                    return False
    return True

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    reservoir = [list(input().strip()) for _ in range(N)]
    print("yes" if is_stable(reservoir, N, M) else "no")