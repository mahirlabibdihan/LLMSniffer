import sys
import math
from bisect import bisect_right

def solve():
    T = int(input().strip())
    for _ in range(T):
        N, Q = map(int, input().strip().split())
        D = list(map(int, input().strip().split()))
        D.sort()
        prefix = [0]*(N+1)
        for i in range(1, N+1):
            prefix[i] = math.gcd(prefix[i-1], D[i-1])
        for _ in range(Q):
            X = int(input().strip())
            l = bisect_right(D, X)
            ans = math.gcd(prefix[l], X)
            print(ans, end=' ')
        print()

solve()