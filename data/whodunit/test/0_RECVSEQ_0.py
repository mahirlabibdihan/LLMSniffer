T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    b = [a[0], a[1], a[2]]
    d = min(b[1] - b[0], b[2] - b[1])
    for i in range(3, N):
        b.append(b[i-1] + d)
    if b[-1] != a[-1]:
        b = [a[0], a[1], a[N-1]]
        d = min(b[1] - b[0], b[2] - b[1])
        for i in range(3, N):
            b.append(b[i-1] + d)
    print(*b)