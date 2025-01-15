def longest_common_pattern_length(T, test_cases):
    for _ in range(T):
        A = test_cases[_][0]
        B = test_cases[_][1]
        common = 0
        for char in set(A):
            common += min(A.count(char), B.count(char))
        print(common)

T = int(input())
test_cases = []
for _ in range(T):
    A = input().strip()
    B = input().strip()
    test_cases.append((A, B))

longest_common_pattern_length(T, test_cases)