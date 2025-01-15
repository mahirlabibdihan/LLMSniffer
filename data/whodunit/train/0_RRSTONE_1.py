def solve(n, k, a):
    max_val = max(a)
    min_val = min(a)
    for i in range(k):
        if i % 2 == 0:
            a = [max_val - i for i in a]
        else:
            a = [i - min_val for i in a]
    return a

n, k = map(int, input().split())
a = list(map(int, input().split()))
result = solve(n, k, a)
print(' '.join(map(str, result)))