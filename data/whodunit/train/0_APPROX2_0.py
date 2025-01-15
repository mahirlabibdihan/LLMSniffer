from collections import Counter
from bisect import bisect_left, bisect_right

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = sorted(map(int, input().split()))
        counter = Counter(A)
        min_diff = float('inf')
        pairs = 0
        for i in range(N):
            j = bisect_left(A, K - A[i])
            if j != i and j != N:
                diff = abs(A[i] + A[j] - K)
                if diff < min_diff:
                    min_diff = diff
                    pairs = counter[A[i]] * counter[A[j]]
                elif diff == min_diff:
                    pairs += counter[A[i]] * counter[A[j]]
        print(min_diff, pairs)

solve()