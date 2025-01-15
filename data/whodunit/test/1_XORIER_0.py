import math
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split(" ")))
    k, l = {}, {}
    u, v = 0, 0
    x, y = 0, 0
    for i in A:
        j = i >> 2
        if i % 2:
            t = k.get(j, 0)
            u += t
            x += 1 if t else 0
            k[j] = t + 1
        else:
            t = l.get(j, 0)
            v += t
            y += 1 if t else 0
            l[j] = t + 1
    a, b = len(k), len(l)
    #print(k)
    #print(l)
    print((a + x) * (a + x - 1) // 2 + (b + y) * (b + y - 1) // 2 - u - v)