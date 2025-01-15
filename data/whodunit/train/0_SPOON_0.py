T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    matrix = [input().lower() for _ in range(R)]
    found = False
    for row in matrix:
        if 'spoon' in row:
            found = True
            break
    if not found:
        for col in range(C):
            if 'spoon' in ''.join([matrix[row][col] for row in range(R)]):
                found = True
                break
    print("There is a spoon!" if found else "There is indeed no spoon!")