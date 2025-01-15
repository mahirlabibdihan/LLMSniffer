import functools
def game_terminate_value(T, test_cases):
    for _ in range(T):
        N, sequence = test_cases[_]
        result = functools.reduce(lambda x, y: math.gcd(x, y), sequence)
        print(result)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    sequence = list(map(int, input().split()))
    test_cases.append((N, sequence))
game_terminate_value(T, test_cases)