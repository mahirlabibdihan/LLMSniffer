from math import gcd

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        min_deletions = -1
        for i in range(N):
            for j in range(i+1, N):
                if gcd(A[i], A[j]) == 1:
                    min_deletions = 0
                    break
            if min_deletions == 0:
                break
        print(min_deletions)

solve()