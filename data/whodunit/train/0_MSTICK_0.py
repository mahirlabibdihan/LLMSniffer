import sys
from math import ceil

def solve():
    N = int(input().strip())
    B = list(map(int, input().strip().split()))
    Q = int(input().strip())
    prefix_max = [0]*N
    suffix_max = [0]*N
    prefix_max[0] = B[0]
    suffix_max[N-1] = B[N-1]
    for i in range(1, N):
        prefix_max[i] = max(prefix_max[i-1], B[i])
    for i in range(N-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], B[i])
    for _ in range(Q):
        L, R = map(int, input().strip().split())
        if L == R:
            print(B[L])
        else:
            max_b = max(prefix_max[R], suffix_max[L])
            total_b = sum(B[L:R+1])
            print(max(max_b, ceil(total_b/2)))

solve()