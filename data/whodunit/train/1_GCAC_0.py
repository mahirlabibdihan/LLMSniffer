for _ in range(int(input())):
    n,m=map(int,input().split())
    sal=list(map(int,input().split()))
    c={}
    ma=[]
    com=[0]*m
    tms=0
    count=0
    for i in range(m):
        v=list(map(int,input().split()))
        ma.append(v[1])
        c[i]=v[0]
    l=[input() for i in range(n)]
    s=-1
    for i in l:
        s+=1
        ms=0
        val=-1
        for k in range(m):
            if(i[k]=='1' and ma[k]>0):
                if(ms<c[k]):
                    ms=c[k]
                    val=k
        if(val!=-1 and sal[s]<=c[val]):
            tms+=ms
            count+=1
            ma[val]-=1
            com[val]=1
    print(count,tms,m-sum(com))
        
                
                
                