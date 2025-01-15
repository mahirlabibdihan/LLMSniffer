T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    matrix = [input().lower() for _ in range(R)]
    transposed_matrix = [''.join([matrix[row][col] for row in range(R)]) for col in range(C)]
    found = any('spoon' in row for row in matrix + transposed_matrix)
    print("There is a spoon!" if found else "There is indeed no spoon!")