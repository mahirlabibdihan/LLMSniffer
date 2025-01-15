from collections import Counter
from sys import stdin, stdout

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a.sort()
    c = Counter(a)
    b = list(c.values())
    b.sort()
    stdout.write(f"{b[-1]} {b[0]}\n")

t = int(stdin.readline())
for _ in range(t):
    solve()