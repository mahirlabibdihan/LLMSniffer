def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        row_min = [min(row) for row in matrix]
        matrix = [[matrix[i][j] - row_min[i] for j in range(N)] for i in range(N)]
        col_min = [min(col) for col in zip(*matrix)]
        for i in range(N):
            for j in range(1, N):
                if matrix[i][j] != matrix[i][j-1] + col_min[j] - col_min[j-1]:
                    print("NO")
                    break
            else:
                continue
            break
        else:
            print("YES")

solve()