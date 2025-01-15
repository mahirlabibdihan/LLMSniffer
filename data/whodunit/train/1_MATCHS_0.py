for _ in range(int(input())):
    n,m=map(int,input().split())
    if n==m:
        print("Ari")
    else:
        e=[n,m]
        e.sort()
        n=e[0]
        m=e[1]
        l=[]
        while n>0 and m>0:
            l.append(m//n)
            e=n
            n=m%n
            m=e 
        l.reverse()
        wi=['w']
        for i in range(1,len(l)):
            if wi[-1]=='w':
                if l[i]==1:
                    wi.append('l')
                else:
                    wi.append('w')
            else:
                wi.append('w')
                
        if wi[-1]=='w':
            print("Ari")
        else:
            print("Rich")
            