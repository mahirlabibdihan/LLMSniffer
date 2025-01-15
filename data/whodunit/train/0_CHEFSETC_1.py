T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0] + nums[1] == 0 or nums[0] + nums[2] == 0 or nums[0] + nums[3] == 0 or nums[1] + nums[2] == 0 or nums[1] + nums[3] == 0 or nums[2] + nums[3] == 0 or nums[0] + nums[1] + nums[2] == 0 or nums[0] + nums[1] + nums[3] == 0 or nums[0] + nums[2] + nums[3] == 0 or nums[1] + nums[2] + nums[3] == 0 or sum(nums) == 0:
        print("Yes")
    else:
        print("No")