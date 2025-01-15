for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    dif=[0]*n
    for i in range(1,n):
        if s[i]!=s[i-1]:
            dif[i]=1
    #print(dif)
    for i in range(1,n):
        dif[i]=dif[i]+dif[i-1]
    #print(dif)
    c=0
    for i in range(m):
        #print(n-m+i,dif[n-m+i],i,dif[i])
        c+=dif[n-m+i]-dif[i]
    print(c)