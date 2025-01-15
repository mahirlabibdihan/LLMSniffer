
from math import sqrt 
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    f, c = [], 1
    while c <= sqrt(n):
        if n % c == 0:
            if n // c != c:
                f.append(n // c)
            f.append(c)
        c += 1
    s = (k * (k + 1)) // 2
    m = -1
    for c in f:
        if c >= s:
            m = max(m, n // c)
    print(m)