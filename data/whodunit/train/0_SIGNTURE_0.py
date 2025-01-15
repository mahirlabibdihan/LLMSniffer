def min_flips(A, B, N, M):
    min_flips = float('inf')
    for dr in range(-N+1, N):
        for dc in range(-M+1, M):
            flips = 0
            for i in range(N):
                for j in range(M):
                    if i+dr < 0 or i+dr >= N or j+dc < 0 or j+dc >= M:
                        if A[i][j] == '1':
                            flips += 1
                    elif A[i][j] != B[i+dr][j+dc]:
                        flips += 1
            min_flips = min(min_flips, flips)
    return min_flips

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    A = [list(input().strip()) for _ in range(N)]
    B = [list(input().strip()) for _ in range(N)]
    print(min_flips(A, B, N, M))