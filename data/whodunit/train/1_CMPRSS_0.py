for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    i=0
    w=[]
    while(i<n):
        if(i+2<n and x[i]+2==x[i+2]):
            a=i+2;
            s=x[i]
            l=x[i+2]
            i+=3
            while(a+1<n and x[a]+1==x[a+1]):
                l=x[a+1]
                a+=1 
                i=a+1 
            w.append(str(s)+"..."+str(l))
        else:
            w.append(str(x[i]))
            i+=1 
    print(",".join(w))
