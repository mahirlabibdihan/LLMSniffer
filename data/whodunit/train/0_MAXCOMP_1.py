def max_compensation(T, test_cases):
    for _ in range(T):
        N, events = test_cases[_]
        events.sort(key=lambda x: x[1])
        dp = [0]*(N+1)
        p = [0]*N
        for i in range(N):
            l, r = 0, i-1
            while l <= r:
                mid = (l + r) // 2
                if events[mid][1] < events[i][0]:
                    if events[mid + 1][1] < events[i][0]:
                        l = mid + 1
                    else:
                        p[i] = mid + 1
                        break
                else:
                    r = mid - 1
        for i in range(1, N+1):
            dp[i] = max(dp[i-1], events[i-1][2] + dp[p[i-1]])
        print(dp[-1])