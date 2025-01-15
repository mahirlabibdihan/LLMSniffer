import sys
from math import log2

def solve():
    Q = int(input().strip())
    flip = 0
    for _ in range(Q):
        query = sys.stdin.readline().strip().split()
        if query[0] == 'Qi':
            flip = 1 - flip
        else:
            x, y = map(int, query[1:])
            black, red = 0, 0
            while x != y:
                if x > y:
                    x, y = y, x
                if int(log2(y)) & 1 == flip:
                    black += 1
                else:
                    red += 1
                y >>= 1
            if int(log2(y)) & 1 == flip:
                black += 1
            else:
                red += 1
            if query[0] == 'Qb':
                print(black)
            else:
                print(red)

solve()