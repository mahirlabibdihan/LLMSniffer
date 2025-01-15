for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    y=sum(a)/n 
    if y%1!=0:
        print(-1)
    else:
        ans=0
        flag=0
        for i in range(n-d):
            r=a[i]-y
            a[i]=y
            a[i+d]+=r 
            ans+=abs(r)
        
        if a.count(y)==n:
            print(int(ans))
        else:
            print(-1)
            