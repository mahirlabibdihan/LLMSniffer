def min_time_to_get_apples(N, K, T):
    left = [0] * (10**6 + 1)
    right = [0] * (10**6 + 1)
    min_time = float('inf')
    for i in range(N):
        if T[i] < K:
            if right[K - T[i]] != 0:
                min_time = min(min_time, i + 1 + right[K - T[i]])
            if left[T[i]] == 0:
                left[T[i]] = i + 1
    for i in range(N - 1, -1, -1):
        if T[i] < K:
            if left[K - T[i]] != 0:
                min_time = min(min_time, N - i + left[K - T[i]])
            if right[T[i]] == 0:
                right[T[i]] = N - i
    if min_time == float('inf'):
        return -1
    else:
        return min_time

N, K = map(int, input().split())
T = list(map(int, input().split()))
print(min_time_to_get_apples(N, K, T))