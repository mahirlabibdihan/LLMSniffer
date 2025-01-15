def min_bad_luck(T, test_cases):
    for _ in range(T):
        n = test_cases[_][0]
        strings = test_cases[_][1:]
        min_a = min(s.count('a') for s in strings)
        min_b = min(s.count('b') for s in strings)
        print(min_a + min_b)

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    strings = [input() for _ in range(n)]
    test_cases.append([n] + strings)
min_bad_luck(T, test_cases)