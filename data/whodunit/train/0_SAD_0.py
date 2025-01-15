R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

min_rows = [min(row) for row in matrix]
max_cols = [max(col) for col in zip(*matrix)]

for r in range(R):
    for c in range(C):
        if matrix[r][c] == min_rows[r] == max_cols[c]:
            print(matrix[r][c])
            exit(0)
print("GUESS")