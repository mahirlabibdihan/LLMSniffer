def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        max_score = 0
        min_score = 0
        for _ in range(N):
            t, a, b = map(int, input().split())
            if t == 1:
                max_score = max(a, b)
                min_score = min(a, b)
            else:
                max_score = max(max_score, max(a, b))
                min_score = max(min_score, min(a, b))
            print("YES" if max_score >= min_score else "NO")

solve()