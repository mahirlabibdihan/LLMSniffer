T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cake = [list(input()) for _ in range(N)]
    cost1, cost2 = 0, 0
    for i in range(N):
        for j in range(M):
            if (i+j)%2 == 0:
                if cake[i][j] == 'R':
                    cost2 += 5
                else:
                    cost1 += 3
            else:
                if cake[i][j] == 'R':
                    cost1 += 5
                else:
                    cost2 += 3
    print(min(cost1, cost2))