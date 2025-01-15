def min_moves(t, test_cases):
    for _ in range(t):
        n, arr = test_cases[_]
        sorted_arr = sorted(arr)
        l = 0
        while arr[l] == sorted_arr[l]:
            l += 1
        r = n - 1
        while arr[r] == sorted_arr[r]:
            r -= 1
        print(r - l + 1)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))
min_moves(t, test_cases)