def count_subsequences(t, test_cases):
    for _ in range(t):
        n, k, s = test_cases[_]
        a_count = s.count('a')
        b_count = s.count('b')
        total = a_count * b_count * k
        print(total)

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    test_cases.append((n, k, s))
count_subsequences(t, test_cases)