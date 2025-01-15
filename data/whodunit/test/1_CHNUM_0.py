try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        m,k=0,0
        for i in l:
            if i>0:
                m+=1
            else:
                k+=1
        if(k==0 or m==0):
            print(max(m,k),max(m,k))
        else:
            print(max(m,k),min(m,k))
except:
    pass
