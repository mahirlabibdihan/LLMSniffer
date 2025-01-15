def solve():
    T = int(input().strip())
    for _ in range(T):
        X, K = map(int, input().strip().split())
        seg_size = X / (2 ** K)
        result = seg_size * (2 * (K - 1) + 1)
        print("%.15f" % result)

solve()