import sys
import math
from bisect import bisect_right

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, Q = map(int, sys.stdin.readline().split())
        D = list(map(int, sys.stdin.readline().split()))
        D.sort()
        prefix = [0]*(N+1)
        for i in range(1, N+1):
            prefix[i] = math.gcd(prefix[i-1], D[i-1])
        queries = list(map(int, sys.stdin.readline().split()))
        for X in queries:
            l = bisect_right(D, X)
            ans = math.gcd(prefix[l], X)
            print(ans, end=' ')
        print()

solve()