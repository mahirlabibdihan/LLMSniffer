MOD = 10**7 + 7
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = 0
for j in range(m):
    column = sorted(matrix[i][j] for i in range(n))
    temp = 1
    for i in column:
        temp = (temp * i) % MOD
    result = (result + temp) % MOD
print(result)