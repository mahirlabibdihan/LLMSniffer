def find_smallest_N(T, test_cases):
    result = []
    for i in range(T):
        L, R = test_cases[i]
        if R >= 2*L:
            result.append(-1)
        else:
            result.append(R)
    return result

T = int(input().strip())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().strip().split())))

print("\n".join(map(str, find_smallest_N(T, test_cases))))