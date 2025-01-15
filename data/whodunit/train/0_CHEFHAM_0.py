from collections import deque
from sys import stdin, stdout

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = [0]*n
    c = deque(sorted(a))
    for i in range(n):
        if c[0] != a[i]:
            b[i] = c[0]
            c.popleft()
        else:
            c.rotate(-1)
    if c[0] != a[0]:
        b[0] = c[0]
        c.popleft()
    else:
        b[0] = c[1]
        c.popleft()
        c.popleft()
    stdout.write(str(n-c.count(a[0]))+'\n')
    stdout.write(' '.join(map(str, b))+'\n')

t = int(stdin.readline())
for _ in range(t):
    solve()