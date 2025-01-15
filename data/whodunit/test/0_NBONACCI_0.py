def solve():
    n, q = map(int, input().split())
    f = list(map(int, input().split()))
    f += [0]*60
    for i in range(n, 64):
        f[i] = f[i-n]^f[i-1]
    for _ in range(q):
        k = int(input())
        if k <= n:
            print(f[k-1])
        else:
            print(f[n-1]^f[k%n-1]^f[n-1])

solve()