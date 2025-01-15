def snek(i, n, h):
    for j in range(i  + 1, n):
        if h[j] >= h[i]:
            return False
    return True
t = int(input())

for i in range(t):
    n, c = map(int, input().split())
    h = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = []
    for j in range(n - 1):
        if snek(j, n, h) and c[j] not in d:
            d.append(c[j])
    if c[n -1] not in d:
        d.append(c[n - 1])
    print(len(d))