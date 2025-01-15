def min_swaps(n, m, a, b):
    a.sort()
    b.sort()
    swaps = 0
    j = 0
    for i in range(n):
        while j < m and b[j] < a[i]:
            j += 1
        if j == m:
            break
        swaps += i - j
        j += 1
    return swaps

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min_swaps(n, m, a, b))