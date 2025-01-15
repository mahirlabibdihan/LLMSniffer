def min_cuts(T, test_cases):
    for _ in range(T):
        N, M, chains = test_cases[_]
        chains.sort()
        cuts = 0
        while len(chains) > 1:
            cuts += 1
            chains.pop()
        print(cuts)

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    chains = list(map(int, input().split()))
    test_cases.append((N, M, chains))
min_cuts(T, test_cases)