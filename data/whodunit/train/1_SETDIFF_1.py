from sys import stdin
from math import gcd, sqrt


def solve():
    mod = 10**9+7
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, stdin.readline().strip().split()))
        a.sort()
        ans = 0
        maxsum = 0
        minsum = 0
        for i in range(n):
            minsum += a[i] * pow(2, n - i - 1, mod)
            minsum %= mod
        for i in range(n - 1, -1, -1):
            maxsum += a[i] * pow(2, i, mod)
            maxsum %= mod
        ans = (maxsum - minsum) % mod
        print(ans)


if __name__ == "__main__":
    solve()
