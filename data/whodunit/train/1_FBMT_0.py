for _ in range(int(input())):
    n=int(input())
    if n==0:
        print('Draw')
    else:
        k=[1,0]
        f=input()
        se=''
        for i in range(n-1):
            s=input()
            if s ==f:
                k[0]+=1 
            else:
                se=s
                k[1]+=1
        if k[0]>k[1]:
            print(f)
        elif k[0]<k[1]:
            print(se)
        else:
            print('Draw')