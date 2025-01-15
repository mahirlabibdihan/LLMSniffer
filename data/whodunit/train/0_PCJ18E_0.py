def min_moves(t, test_cases):
    for _ in range(t):
        n, arr = test_cases[_]
        sorted_arr = sorted(arr)
        i = 0
        j = n - 1
        while i < j:
            if arr[i] == sorted_arr[i]:
                i += 1
            elif arr[j] == sorted_arr[j]:
                j -= 1
            else:
                break
        print(j - i + 1)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))
min_moves(t, test_cases)