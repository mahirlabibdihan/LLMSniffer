def solve():
    Q = int(input())
    for _ in range(Q):
        N, K = map(int, input().split())
        pos = 0
        while K:
            if K & 1:
                break
            K >>= 1
            pos += 1
        print(1 << pos)

solve()