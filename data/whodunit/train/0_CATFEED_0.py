from collections import Counter

def is_fair_order(T, test_cases):
    for _ in range(T):
        N, M, A = test_cases[_]
        counter = Counter(A)
        max_count = max(counter.values())
        for cat in counter:
            if counter[cat] < max_count - 1:
                print("NO")
                break
        else:
            print("YES")

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, M, A))
is_fair_order(T, test_cases)