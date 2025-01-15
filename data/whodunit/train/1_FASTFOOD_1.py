for j in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=sum(y)
    t=a
    for i in range(n):
        a-=y[i]
        a+=x[i]
        if(a>t):
            t=a
    print(t)
