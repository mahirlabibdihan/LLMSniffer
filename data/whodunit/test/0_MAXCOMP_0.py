def max_compensation(T, test_cases):
    for _ in range(T):
        N, events = test_cases[_]
        events.sort(key=lambda x: x[1])
        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = max(dp[i-1], events[i-1][2] + dp[binary_search(events, i)])
        print(dp[-1])

def binary_search(events, index):
    start, end = 0, index - 1
    while start <= end:
        mid = (start + end) // 2
        if events[mid][1] <= events[index-1][0]:
            if events[mid + 1][1] <= events[index-1][0]:
                start = mid + 1
            else:
                return mid + 1
        else:
            end = mid - 1
    return 0