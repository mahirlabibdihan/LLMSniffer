def solve(n, k, a):
    max_val = max(a)
    if k % 2 == 1:
        return [max_val - i for i in a]
    else:
        min_val = min(a)
        return [i - min_val for i in a]

n, k = map(int, input().split())
a = list(map(int, input().split()))
result = solve(n, k, a)
print(' '.join(map(str, result)))