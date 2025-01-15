T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    rooks = [list(map(int, input().split())) for _ in range(K)]
    rows = [0]*N
    cols = [0]*N
    for r, c in rooks:
        rows[r-1] = 1
        cols[c-1] = 1
    rooks = [(i+1, j+1) for i in range(N) for j in range(N) if rows[i] == 0 and cols[j] == 0]
    print(len(rooks), *sum(rooks, []))