from bisect import bisect_left
def solve(arr):
    arr = sorted(arr, key = lambda x : x[0])

    nums = []
    ans  = 0

    for x, y in arr:
        idx = bisect_left(nums, y)
        if idx == len(nums):
            nums.append(y)
        else:
            ans += len(nums)-idx
            nums.insert(idx, y)

    return ans
    

arr = []
for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    arr.append((x, y))
    
print(solve(arr))
    

