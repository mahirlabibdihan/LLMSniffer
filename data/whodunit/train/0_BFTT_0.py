def find_number(T, test_cases):
    for _ in range(T):
        N = test_cases[_]
        while True:
            N += 1
            if str(N).count('3') >= 3:
                print(N)
                break

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
find_number(T, test_cases)