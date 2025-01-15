def count_squares(garden, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            size = 1
            while i + size < n and j + size < m:
                if garden[i][j] == garden[i + size][j] == garden[i][j + size] == garden[i + size][j + size]:
                    count += 1
                size += 1
    return count

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    garden = [list(input()) for _ in range(N)]
    print(count_squares(garden, N, M))