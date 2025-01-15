T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if A[i][j] == -1:
                if i == N-1 and j == M-1:
                    A[i][j] = 1
                elif i == N-1:
                    A[i][j] = A[i][j+1]
                elif j == M-1:
                    A[i][j] = A[i+1][j]
                else:
                    A[i][j] = min(A[i+1][j], A[i][j+1])
            elif i < N-1 and A[i][j] > A[i+1][j]:
                A[i+1][j] = A[i][j]
            elif j < M-1 and A[i][j] > A[i][j+1]:
                A[i][j+1] = A[i][j]
    if any(A[i][j] > A[i+1][j] for i in range(N-1) for j in range(M)) or any(A[i][j] > A[i][j+1] for i in range(N) for j in range(M-1)):
        print(-1)
    else:
        for row in A:
            print(*row)