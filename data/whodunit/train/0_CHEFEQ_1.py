def min_operations(T, test_cases):
    for _ in range(T):
        N, piles = test_cases[_]
        unique_piles = set(piles)
        max_count = max(piles.count(pile) for pile in unique_piles)
        print(N - max_count)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    piles = list(map(int, input().split()))
    test_cases.append((N, piles))
min_operations(T, test_cases)