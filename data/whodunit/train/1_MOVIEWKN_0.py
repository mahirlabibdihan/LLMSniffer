for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    r =list(map(int,input().split()))

    m=[]
    

    for j in range(a):
        m.append(l[j]*r[j])

    p=r.index(max(r))

    if m.index(max(m))==p:
        print(p+1)
    else:
        df=[]
        for k in range(a):
            if m[k] == max(m):
                df.append([r[k],k+1])

        df.sort()
        for b in df:
            if b[0]==df[-1][0]:
                print(b[1])
                break
                
    
