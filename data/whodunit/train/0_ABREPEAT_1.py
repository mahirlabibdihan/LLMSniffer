def count_subsequences(t, test_cases):
    for _ in range(t):
        n, k, s = test_cases[_]
        a_count = 0
        b_count = 0
        total = 0
        for char in s:
            if char == 'a':
                a_count += 1
            elif char == 'b':
                b_count += 1
                total += a_count
        total *= k
        print(total)

t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    test_cases.append((n, k, s))
count_subsequences(t, test_cases)