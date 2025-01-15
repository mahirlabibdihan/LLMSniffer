for t in range(int(input())):
    g={}
    d={}
    tot=0
    f=input()
    f=int(f)
    for _ in range(f-1):
        en=input().strip()
        a,b,c=en.split()
        g[a]=[b,c]
        if a not in d.keys():
            d[a]=1
        else:
            d[a]+=1
        if b not in d.keys():
            d[b]=1
        else:
            d[b]+=1
        tot+=int(c[:-1])
    for i in g.keys():
        if d[i]==1:
            source=i
            break
    while source in g.keys():
        print(source,g[source][0],g[source][1])
        source=g[source][0]
    print(str(tot)+"$")
