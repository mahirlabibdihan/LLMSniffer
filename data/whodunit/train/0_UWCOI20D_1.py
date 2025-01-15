from sys import stdin, stdout
from collections import deque
from itertools import permutations

def solve():
    n = int(stdin.readline())
    grid = [list(map(int, stdin.readline().strip())) for _ in range(n)]
    rows = [i for i in range(n) if 1 in grid[i]]
    cols = [j for j in range(n) if 1 in [grid[i][j] for i in range(n)]]
    row_perms = list(permutations(rows))
    col_perms = list(permutations(cols))
    count = 0
    for rp in row_perms:
        for cp in col_perms:
            if all(grid[rp[i]][cp[i]] == 1 for i in range(n)):
                count += 1
    stdout.write(str(count) + '\n')

t = int(stdin.readline())
for _ in range(t):
    solve()