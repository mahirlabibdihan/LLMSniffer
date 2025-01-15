def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        pos = {}
        for i in range(N):
            row = list(map(int, input().split()))
            for j in range(N):
                pos[row[j]] = (i, j)
        steps = 0
        for i in range(2, N*N+1):
            steps += abs(pos[i][0]-pos[i-1][0]) + abs(pos[i][1]-pos[i-1][1])
        print(steps)

solve()