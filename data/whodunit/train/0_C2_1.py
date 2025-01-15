def sum_of_powers(t, test_cases, p):
    for i in range(t):
        n, k = test_cases[i]
        sum = sum([pow(j, k, p) for j in range(1, n+1)])
        print(sum % p)

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    test_cases.append((n, k))
p = int(input())
sum_of_powers(t, test_cases, p)