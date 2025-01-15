T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    diffs = [a[i+1] - a[i] for i in range(N-1)]
    d = min(diffs)
    b = [a[0]]
    for i in range(1, N):
        b.append(b[i-1] + d)
    if b[-1] != a[-1]:
        d = a[N-1] - a[0]
        b = [a[0]]
        for i in range(1, N):
            b.append(b[i-1] + d)
    print(*b)