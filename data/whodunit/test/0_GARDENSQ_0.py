def count_squares(garden, n, m):
    count = 0
    for size in range(1, min(n, m)):
        for i in range(n - size):
            for j in range(m - size):
                if garden[i][j] == garden[i + size][j] == garden[i][j + size] == garden[i + size][j + size]:
                    count += 1
    return count

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    garden = [list(input()) for _ in range(N)]
    print(count_squares(garden, N, M))