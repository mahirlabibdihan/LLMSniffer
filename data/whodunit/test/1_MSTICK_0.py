import math
def get(l,r,a):
    x=len(a)//2
    y=l
    n=r
    m=len(a)
    o=0
    p=0
    q=1000000001
    #print(l,r,x,y,n,m)
    while l<r:
        if l%2==1:
            p=max(p,a[l][1])
            q=min(q,a[l][0])
            l+=1
        if r%2==1:
            p=max(p,a[r-1][1])
            q=min(q,a[r-1][0])
            r-=1
        l//=2
        r//=2
    z=0
    while x<y:
        if x%2==1:
            z=max(z,a[x][1])
            x+=1
        if y%2==1:
            z=max(z,a[y-1][1])
            y-=1
        x//=2
        y//=2
    while n<m:
        if n%2==1:
            o=max(o,a[n][1])
            n+=1
        if m%2==1:
            o=max(o,a[m-1][1])
            m-=1
        n//=2
        m//=2
    o=max(o,z)    
    s=q+max((p-q)/2,o)
    return s
x=int(input())
a=list(map(int,input().split()))
lol=[[0]*2]*x*2
i=2*x-1
while i>0:
    if i>=x:
        lol[i]=[a[i-x],a[i-x]]
    else:
        p=min(lol[2*i][0],lol[2*i+1][0])
        q=max(lol[2*i][1],lol[2*i+1][1])
        lol[i]=[p,q]
    i-=1
#print(lol)    
n=int(input())
for __ in range(n):
    l,r=map(int,input().split())
    r+=1+x
    l+=x
    #print(l,r)
    print("%.1f"%get(l,r,lol))