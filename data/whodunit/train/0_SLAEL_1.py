def longest_segment(T, test_cases):
    for t in range(T):
        N, K, arr = test_cases[t]
        max1 = max2 = -1
        l = r = res = 0
        while r < N:
            if arr[r] > max1:
                max2 = max1
                max1 = arr[r]
            elif arr[r] > max2:
                max2 = arr[r]
            while max1 > K and max2 > K:
                if arr[l] == max1 or arr[l] == max2:
                    if arr[l] == max1:
                        max1 = max2
                    max2 = -1
                    for i in range(l + 1, r + 1):
                        if arr[i] > max1:
                            max2 = max1
                            max1 = arr[i]
                        elif arr[i] > max2:
                            max2 = arr[i]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        print(res)

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((N, K, arr))
longest_segment(T, test_cases)
