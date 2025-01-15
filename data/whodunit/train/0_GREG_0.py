def solve(n, m):
    if min(n, m) > 1:
        return 1
    else:
        return 2

n, m = map(int, input().split())
print(solve(n, m))