for _ in range(int(input())):
    n=int(input())
    l=[]
    ans=0
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-1):
        for j in range(n-1):
            l[i+1][j+1]+=l[i][j]
    for i in range(n):
        for j in range(n):
            ans=max(ans,l[i][j])
    print(ans)