def find_lucky_lucky_number(T, test_cases):
    results = []
    for N in test_cases:
        for x in range(0, N+1, 7):
            if (N - x) % 4 == 0:
                results.append(x)
                break
        else:
            results.append(-1)
    return results

T = int(input())
test_cases = [int(input()) for _ in range(T)]
print('\n'.join(map(str, find_lucky_lucky_number(T, test_cases))))