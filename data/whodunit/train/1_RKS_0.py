from math import ceil
for i in range(int(input())):
    n,k=list(map(int,input().split()))
    data=[0]*(n+1)
    memo=[0]*(n+1)
    for j in range(k):
        x,y=map(int,input().split())
        data[x]=True
        memo[y]=True
    print(n-k,end=" ")
    k=1
    for j in range(1,n+1):
        if data[j]==False:
            for l in range(k,n+1):
                if memo[l]==False:
                    print(j,l,end=" ")
                    data[j]=True
                    memo[l]=True
                    k=l+1
                    break
    print("")

