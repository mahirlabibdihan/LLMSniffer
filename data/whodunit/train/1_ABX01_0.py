for _ in range(int(input())):
    A,N=map(int,input().split())
    res=pow(A,N,9)
    if(res==0):
        print(9)
    else:
        print(res)