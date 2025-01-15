for t in range(int(input())):
    c=[0]*31
    for i in range(int(input())):
        d,p=map(int,input().split())
        c[d-1]=p
    for i in range(int(input())):
        dead,req=map(int,input().split())
        s=c[0:dead]
        if sum(s)<req:
            print("Go Sleep")
        else:
            print("Go Camp")