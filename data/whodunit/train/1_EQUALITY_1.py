t=int(input())
for loop in range(t):
    n=int(input())
    nums=list(map(int,(input()).split()))
    s=0
    for num in nums:
        s+=num
    
    for i in range(n):
        x=(s//(n-1))-nums[i]
        print(x,end=" ")
    print("")