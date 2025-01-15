n=int(input())
count=0
def sumse(x):
    sums=0
    while x:
        sums+=x%10
        x=x//10
    return sums
for i in range(max(0,n-1000),n+1):
    res=i+sumse(i)+sumse(sumse(i))
    if res==n:
        count+=1
print(count)