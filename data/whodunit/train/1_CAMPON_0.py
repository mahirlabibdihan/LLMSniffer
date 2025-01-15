for _ in range(int(input())):
    t=int(input())
    p=[]
    for i in range(t):
        a,b=map(int,input().split())
        p.append([a,b])
    p=sorted(p)
    for j in range(t-1):
        p[j+1][1]+=p[j][1]
    q=int(input())
    for m in range(q):
        flag=0
        dead1,req1=map(int,input().split())
        for k in p:
            if k[0]<=dead1:
                if req1<=k[1]:
                    flag=1
        if flag==1:
            print('Go Camp')
        else:
            print('Go Sleep')