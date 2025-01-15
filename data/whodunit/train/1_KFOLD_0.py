for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    a=s.count("1")
    b=s.count("0")
    if max(a,b)%(n//k)!=0:
        print('IMPOSSIBLE')
    else:
        c='0'*(b//(n//k))+'1'*(a//(n//k))
        d='1'*(a//(n//k))+'0'*(b//(n//k))
        ans=""
        for i in range(n//k):
            if i%2==0:
                ans+=c 
            else:
                ans+=d 
        print(ans)