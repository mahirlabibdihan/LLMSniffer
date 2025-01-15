def solve(n, m):
    return 1 if min(n, m) > 1 else 2

n, m = map(int, input().strip().split())
print(solve(n, m))