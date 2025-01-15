def min_replacements(T, test_cases):
    for _ in range(T):
        S = test_cases[_]
        count = 0
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                count += 1
        print(count)

T = int(input().strip())
test_cases = []
for _ in range(T):
    test_cases.append(input().strip())
min_replacements(T, test_cases)