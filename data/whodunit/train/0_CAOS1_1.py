from sympy import isprime

def count_monsters(T, maps):
    for t in range(T):
        R, C, grid = maps[t]
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '^':
                    L = R = T = B = 0
                    while j-L-1 >= 0 and grid[i][j-L-1] == '^':
                        L += 1
                    while j+R+1 < C and grid[i][j+R+1] == '^':
                        R += 1
                    while i-T-1 >= 0 and grid[i-T-1][j] == '^':
                        T += 1
                    while i+B+1 < R and grid[i+B+1][j] == '^':
                        B += 1
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