from math import comb

def calculate_probability(T, test_cases):
    for _ in range(T):
        S, N, M, K = test_cases[_]
        total_ways = comb(S - 1, N - 1)
        favourable_ways = 0
        for i in range(K, min(M, N)):
            if N - i - 1 < S - M:
                favourable_ways += comb(M - 1, i) * comb(S - M, N - i - 1)
        probability = favourable_ways / total_ways
        print("%.15f" % probability)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
calculate_probability(T, test_cases)