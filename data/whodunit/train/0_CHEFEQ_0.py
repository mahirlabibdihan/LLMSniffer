def min_operations(T, test_cases):
    for _ in range(T):
        N, piles = test_cases[_]
        piles_count = [0]*(max(piles)+1)
        for pile in piles:
            piles_count[pile] += 1
        print(N - max(piles_count))

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    piles = list(map(int, input().split()))
    test_cases.append((N, piles))
min_operations(T, test_cases)