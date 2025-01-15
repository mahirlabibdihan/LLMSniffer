def max_cost(t, test_cases):
    for _ in range(t):
        n, a = test_cases[_]
        a.sort()
        res = a[-1]
        for i in range(n-2, -1, -1):
            res = res % a[i]
        yield res

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

for res in max_cost(t, test_cases):
    print(res)