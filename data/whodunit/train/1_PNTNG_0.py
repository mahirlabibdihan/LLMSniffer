def solve():
    n,m,h=map(int,input().split())
    Tcells=0
    d=[]
    for _ in range(h):
        t,c=map(int,input().split())
        d.append([t,c])
        Tcells+=t
    d_sorted=sorted(d,key=lambda x:x[1])
    Pcells=0
    cost=0
    k=m*n
    if k<=Tcells:
        for i in d_sorted:
            Pcells+=i[0]
            if Pcells<k:
                cost+=i[0]*i[1]
            else:
                cost+=(k-Pcells+i[0])*i[1]
                print(cost)
                break
    else:
        print('Impossible')
solve()