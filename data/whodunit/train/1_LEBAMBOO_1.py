t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = list(map(int, input().split()))
    if n == 1:
        if l[0] >= d[0]:
            print(l[0] - d[0])
        else:
            print(-1)
    elif n == 2:
        if sum(l) == sum(d):
            print(abs(l[0] - d[0]))
        else:
            print(-1)
    else:
        f = sum(d) - sum(l)
        ans = f // (n - 2)
        if f < 0 or f % (n - 2) != 0:
            print(-1)
        else:
            for k in range(n):
                x = ans + l[k] - d[k]
                if x < 0 or x % 2 != 0:
                    ans = -1
                    break
            print(ans)