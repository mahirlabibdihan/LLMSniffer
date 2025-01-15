from sympy import isprime

def count_monsters(T, maps):
    for t in range(T):
        R, C, grid = maps[t]
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '^':
                    L = len(list(takewhile(lambda x: x == '^', reversed(grid[i][:j]))))
                    R = len(list(takewhile(lambda x: x == '^', grid[i][j+1:])))
                    T = len(list(takewhile(lambda x: x == '^', reversed([grid[k][j] for k in range(i)]))))
                    B = len(list(takewhile(lambda x: x == '^', [grid[k][j] for k in range(i+1, R)])))
                    if isprime(min(L, R, T, B)):
                        count += 1
        print(count)

T = int(input())
maps = []
for _ in range(T):
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    maps.append((R, C, grid))
count_monsters(T, maps)