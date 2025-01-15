def count_pairs(arr, n):
    zero = 0
    two = 0
    for i in range(n):
        if arr[i] == 2:
            two += 1
        if arr[i] == 0:
            zero += 1
    ans = 0
    for i in range(n):
        if arr[i] == 0 or arr[i] == 2:
            continue
        ans += n - i - 1
    ans -= (two*(two-1))//2
    ans -= (zero*(zero-1))//2
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(count_pairs(arr, N))