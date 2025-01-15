for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    d=list(map(int,input().split()))
    di=n-2
    if n==1:
        if h[0]>=d[0]:
            print(h[0]-d[0])
        else:
            print(-1)
    elif n==2:
        if sum(d)==sum(h):
            print(abs(d[0]-h[0]))
        else:
            print(-1)
    else:
        
        f=(sum(d)-sum(h))//di
        if f<0 or (sum(d)-sum(h))%di!=0:
            print(-1)
        else:
            w=[d[i]-h[i] for i in range(n)]
            flag=0
            for i in range(n):
                if (f-w[i])<0 or (f-w[i])%2!=0:
                    flag=1 
                    break
            if flag==1:
                print(-1)
            else:
                print(f)