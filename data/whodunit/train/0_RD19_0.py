from math import gcd
from functools import reduce

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        if reduce(gcd, A) == 1:
            print(0)
        else:
            print(-1)

solve()