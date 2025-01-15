factors=[0]*1000001
for i in range(2,1000001):
    if factors[i]==0:
        factors[i]=1
        for j in range(i+i,1000001,i):
            factors[j]+=1
t=int(input())
while t:
    t-=1
    ans=0
    n,m=map(int,input().strip().split(' '))
    for i in range(n,m):
        ans+=factors[i]
    print(ans)
