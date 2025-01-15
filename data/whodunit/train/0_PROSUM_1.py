def count_pairs(arr, n):
    zero = arr.count(0)
    two = arr.count(2)
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