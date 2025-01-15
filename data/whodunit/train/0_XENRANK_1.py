def max_rank(T, test_cases):
    result = []
    for i in range(T):
        U, V = test_cases[i]
        if U > V:
            result.append((U*(U+1))//2 + 1)
        else:
            result.append((V*(V+1))//2 + 1)
    return result

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))

print('\n'.join(map(str, max_rank(T, test_cases))))