def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = sorted(map(int, input().split()))
        min_diff = float('inf')
        pairs = 0
        for i in range(N):
            for j in range(i+1, N):
                diff = abs(A[i] + A[j] - K)
                if diff < min_diff:
                    min_diff = diff
                    pairs = 1
                elif diff == min_diff:
                    pairs += 1
        print(min_diff, pairs)

solve()