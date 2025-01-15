def count_balanced_strings(T, test_cases):
    for _ in range(T):
        S = test_cases[_]
        prefix_count = [0] * (len(S) + 1)
        count_4 = [0] * (len(S) + 1)
        count_7 = [0] * (len(S) + 1)
        for i in range(len(S)):
            count_4[i + 1] = count_4[i] + (S[i] == '4')
            count_7[i + 1] = count_7[i] + (S[i] == '7')
            prefix_count[count_4[i + 1] - count_7[i + 1]] += 1
        result = 0
        for i in range(len(S) + 1):
            result += prefix_count[i] * (prefix_count[i] - 1) // 2
        print(result)

T = int(input().strip())
test_cases = [input().strip() for _ in range(T)]
count_balanced_strings(T, test_cases)