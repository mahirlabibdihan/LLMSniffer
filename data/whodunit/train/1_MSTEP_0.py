for _ in range(int(input())):
    n=int(input())
    d={}
    a=[]
    for i in range(n):
        a.append([int(x) for x in input().split()])
        for j in range(n):
            d[a[i][j]]=[i,j]
    
    c=0
    for i in range(2,n*n+1):
        c+=abs(d[i-1][0]-d[i][0])+abs(d[i-1][1]-d[i][1])
    
    print(c)
            