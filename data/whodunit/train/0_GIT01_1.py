T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cake = [list(input()) for _ in range(N)]
    costs = [0, 0]
    for i in range(N):
        for j in range(M):
            if cake[i][j] == 'R':
                costs[(i+j)%2] += 5
                costs[(i+j+1)%2] += 3
            else:
                costs[(i+j)%2] += 3
                costs[(i+j+1)%2] += 5
    print(min(costs))