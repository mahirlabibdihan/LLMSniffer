for _ in range(int(input())):
    n=int(input())
    md=10**9+7
    ans=pow(3,n,md)
    if n%2==0:
        print((ans+3)%md)
    else:
        print((ans-3)%md)