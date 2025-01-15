def solve():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        A = [list(map(int, list(input().strip()))) for _ in range(N)]
        row = [0]*N
        col = [0]*M
        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    row[i] = 1
                    col[j] = 1
        for i in range(N):
            for j in range(M):
                if row[i] == 1 or col[j] == 1:
                    print(1, end=' ')
                else:
                    print(2 if row.count(1) > 0 or col.count(1) > 0 else -1, end=' ')
            print()

solve()