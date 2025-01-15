try:
    for i in range(int(input())):
        n,m = map(int,input().split())
        l = {}
        for j in range(0,n):
            d,v =  map(int,input().split())
            if(d in l.keys()):
                g = l[d]
                if(g<v):
                    l[d] = v 
            else:
                l[d] = v
        f = sorted(l.values()) 
        s = f[-1]+f[-2]
        print(s)
except EOFError as e:
    pass
