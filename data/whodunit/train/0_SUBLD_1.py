def largest_possible_value(T, test_cases):
    for _ in range(T):
        k = test_cases[_]
        if k <= 9:
            print(k-1)
        else:
            k -= 9
            nines = k // 9
            rem = k % 9
            print(int(str(rem) + '9' * nines))

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
largest_possible_value(T, test_cases)