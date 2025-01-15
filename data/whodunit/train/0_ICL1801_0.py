T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.extend(list(map(int, input().split())))
    matrix.sort(reverse=True)
    cyborg, geno = 0, 0
    for i in range(len(matrix)):
        if i % 2 == 0:
            cyborg += matrix[i]
        else:
            geno += matrix[i]
    if cyborg > geno:
        print("Cyborg")
    elif geno > cyborg:
        print("Geno")
    else:
        print("Draw")