import math
def min_cards(T, test_cases):
    for i in range(T):
        N = test_cases[i]
        ans = 0
        while N > 0:
            N = N // 2
            ans += 1
        print(ans)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    test_cases.append(N)
min_cards(T, test_cases)