from sys import stdin, stdout
from math import ceil


def solve():
    n, m = map(int, stdin.readline().split())
    a = []
    c = [0] * m
    mod = 10**7+7
    for i in range(n):
        b = list(map(int, stdin.readline().strip().split()))
        a.append(b)
        for j in range(m):
            c[j] += b[j]
    ans = 1
    for i in range(m):
        ans *= c[i]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    solve()
