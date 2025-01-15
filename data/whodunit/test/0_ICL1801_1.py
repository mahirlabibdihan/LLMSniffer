T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [int(x) for _ in range(N) for x in input().split()]
    matrix.sort(reverse=True)
    cyborg = sum(matrix[i] for i in range(len(matrix)) if i % 2 == 0)
    geno = sum(matrix[i] for i in range(len(matrix)) if i % 2 != 0)
    print("Cyborg" if cyborg > geno else "Geno" if geno > cyborg else "Draw")