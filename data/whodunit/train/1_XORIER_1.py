t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=[]
    for i in l:
        if not i%2:
            k.append(i)
    d={}
    for i in k:
        try:
            d[i]+=1
        except:
            d[i]=1
    m=len(k)
    ans=0
    x=list(d.keys())
    x.sort()
    for i in x:
        m-=d[i]
        k=m
        try:
            x=d[i+2]
            if (i+2)^i==2:
                k-=x
        except:
            pass
        ans+=d[i]*k
    k=[]
    for i in l:
        if i%2:
            k.append(i)
    d={}
    for i in k:
        try:
            d[i]+=1
        except:
            d[i]=1
    m=len(k)
    x=list(d.keys())
    x.sort()
    for i in x:
        m-=d[i]
        k=m
        try:
            x=d[i+2]
            if (i+2)^i==2:
                k-=x
        except:
            pass
        ans+=d[i]*k
    print(ans)
