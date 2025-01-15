for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==1:
        print(1)
    elif k<=(n//2):
        c=1
        t_1=2
        while c<=k:
            print(t_1,end=' ')
            t_1=t_1+2
            c+=1
        print()
    else:
        print(-1)