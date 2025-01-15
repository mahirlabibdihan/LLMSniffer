t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    
    arr=[0]*32
    temp=k
    i=0
    while temp>0:
        if temp&1:
            arr[i]=1
        temp>>=1
        i+=1
    kbits=sum(arr)
    if kbits>n:
        print(-1)
        continue
    idx=26
    while kbits!=n and idx>0:
        if arr[idx]>=1:
            arr[idx-1]+=2
            arr[idx]-=1
            kbits+=1
        else:
            idx-=1
    res=""
    for i in range(26):
        if arr[i]>=1:
            res+=arr[i]*chr(i+97)
    print(res if sum(arr)==n else -1)
            
    
    
        
    
    