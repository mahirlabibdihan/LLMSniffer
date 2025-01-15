n,m=map(int,input().split())
s=1000
low=1
high=n
ans=0
p=6
while high>=low:
    mid=low+(high-low)//p
    print(1, mid)
    r=int(input())
    if r==1:
        high=mid-1
        print(2)
    else:
        low=mid+1
        ans=mid
print(3, ans+1)


