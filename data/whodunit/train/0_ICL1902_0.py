import math
def count_squares(T, test_cases):
    for i in range(T):
        N = test_cases[i]
        squares = 0
        while N > 0:
            S = int(math.sqrt(N))
            N -= S*S
            squares += 1
        print(squares)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
count_squares(T, test_cases)