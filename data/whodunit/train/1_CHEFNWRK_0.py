t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    summ=0
    i=0
    count=1
    if max(arr)>k:
        print(-1)
        continue
    while i<len(arr):
        summ+=arr[i]
        if summ>k:
            count+=1
            summ=arr[i]
        i+=1
    print(count)