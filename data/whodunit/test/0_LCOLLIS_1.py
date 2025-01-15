T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(N)]
    collisions = 0
    for j in range(M):
        count = 0
        for i in range(N):
            if matrix[i][j] == 1:
                count += 1
        collisions += max(0, count - 1)
    print(collisions)