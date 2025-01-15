from math import comb

def calculate_probability(T, test_cases):
    for _ in range(T):
        S, N, M, K = test_cases[_]
        ans = 0.0
        for i in range(K, M):
            if N - i - 1 < S - M:
                ans += comb(M - 1, i) * comb(S - M, N - i - 1)
        ans /= comb(S - 1, N - 1)
        print("%.15f" % ans)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
calculate_probability(T, test_cases)