from bisect import bisect_right

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        walls = list(map(int, input().split()))
        Q = int(input())
        for _ in range(Q):
            x, y = map(int, input().split())
            if x != y:
                print(bisect_right(walls, max(x, y)))
            else:
                if bisect_right(walls, x) != bisect_right(walls, x - 1):
                    print(-1)
                else:
                    print(bisect_right(walls, x))

solve()