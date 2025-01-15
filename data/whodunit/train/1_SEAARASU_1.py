def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
t=int(input())
for I in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print(l[0])
    else:
        g=l[0]
        for I in range(1,n):
            if(g>l[I]):
                g=gcd(l[I],g)
            else:
                g=gcd(g,l[I])
        print(n*g)