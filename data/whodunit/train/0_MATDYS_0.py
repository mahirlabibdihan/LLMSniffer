def solve():
    Q = int(input())
    for _ in range(Q):
        N, K = map(int, input().split())
        pos = 0
        while K % 2 == 0:
            K //= 2
            pos += 1
        print(2 ** pos)

solve()