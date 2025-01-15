n,m=map(int,input().split())
s=input().strip()
l=[int(i) for i in s]
d=[0]*(10)
ans=[0]*(n+193)
for i in range(n):
    curr=l[i]
    less=0 
    big=0 
    c1=0 
    c2=0 
    for j in range(10):
        if j<curr:
            c1+=d[j]
            less+=d[j]*j 
        if j>curr:
            c2+=d[j]
            big+=d[j]*j 
    ans[i]=big-less+curr*(c1-c2)
    d[l[i]]+=1 
for _ in range(m):
    x=int(input())
    print(ans[x-1])