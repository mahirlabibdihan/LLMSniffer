for _ in range(int(input())):
    input()
    C=list(map(int, input().split()))
    W=list(map(int,input().split()))
    s,i=set([C[0]]),0
    c=mx=W[0]
    for j in range(1,len(C)):
        while C[j] in s:
            mx=max(mx,c)
            s.remove(C[i])
            c-=W[i];i+=1
        s.add(C[j])
        c+=W[j]
    print(max(mx,c))