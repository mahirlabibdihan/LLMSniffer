def find_number(T, test_cases):
    for _ in range(T):
        N = test_cases[_]
        while str(N).count('3') < 3:
            N += 1
        print(N)

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
find_number(T, test_cases)