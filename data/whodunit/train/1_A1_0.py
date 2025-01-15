def ss(ar,l,r,sum=0):
    if(ar[len(ar)-1]==-1):
        return
    if(l>r):
        if(sum==k):
            print("Yes")
            ar.append(-1)
            return
        return
    ss(ar,l+1,r,sum+ar[l])
    ss(ar,l+1,r,sum)
    




t=int(input())
while(t>0):
    n,k=map(int,input().split())
    ar=[]
    for i in range(n):
        ar.append(int(input()))
    ss(ar,0,n-1)
    if(ar[len(ar)-1]!=-1):
        print("No")
    t=t-1