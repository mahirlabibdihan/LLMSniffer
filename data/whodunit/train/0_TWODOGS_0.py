def min_time_to_get_apples(N, K, T):
    left = {}
    right = {}
    min_time = float('inf')
    for i in range(N):
        if T[i] < K:
            if K - T[i] in right:
                min_time = min(min_time, i + 1 + right[K - T[i]])
            left[T[i]] = i + 1
    for i in range(N - 1, -1, -1):
        if T[i] < K:
            if K - T[i] in left:
                min_time = min(min_time, N - i + left[K - T[i]])
            right[T[i]] = N - i
    if min_time == float('inf'):
        return -1
    else:
        return min_time

N, K = map(int, input().split())
T = list(map(int, input().split()))
print(min_time_to_get_apples(N, K, T))