T=int(input())
for ti in range(T):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    res=0
    nump=0
    for ai in range(len(A)):
        if(A[ai]>=res):
            fd=A[ai]-res
            pi=fd//k
            nump+=pi
            #print("a")
            if pi>0:
                if fd%k==0:
                    res=0
                else:
                    res=k-fd%k-1
                    nump+=1
            else:
                if fd%k==0:
                    res=0
                else:
                    res=k-fd-1
                    nump+=1
        else:
            fd=res-A[ai]
            res=fd-1
        #print(fd)
        #print(nump)
    print(nump)