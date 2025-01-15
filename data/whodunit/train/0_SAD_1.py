R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

min_rows = {min(row): i for i, row in enumerate(matrix)}
max_cols = {max(col): i for i, col in enumerate(zip(*matrix))}

for cost in set(min_rows) & set(max_cols):
    if min_rows[cost] == max_cols[cost]:
        print(cost)
        break
else:
    print("GUESS")