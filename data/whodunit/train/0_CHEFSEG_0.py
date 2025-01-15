def solve():
    T = int(input().strip())
    for _ in range(T):
        X, K = map(int, input().strip().split())
        seg_size = X / (2 ** K)
        print("{:.15f}".format(seg_size * (2 * (K - 1) + 1)))

solve()