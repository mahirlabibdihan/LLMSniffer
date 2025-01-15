from collections import Counter

def longest_common_pattern_length(T, test_cases):
    for _ in range(T):
        A = Counter(test_cases[_][0])
        B = Counter(test_cases[_][1])
        common = A & B
        print(sum(common.values()))

T = int(input())
test_cases = []
for _ in range(T):
    A = input().strip()
    B = input().strip()
    test_cases.append((A, B))

longest_common_pattern_length(T, test_cases)