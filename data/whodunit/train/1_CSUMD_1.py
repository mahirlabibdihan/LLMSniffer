mod=10**9+7
def mul(m,l):
    c1=m[0][0]
    c2=m[0][1]
    c3=m[1][0]
    c4=m[1][1]
    a1=l[0][0]
    a2=l[0][1]
    a3=l[1][0]
    a4=l[1][1]
    a=((c1%mod*a1%mod)%mod+(c2%mod*a3%mod)%mod)%mod
    b=((c1%mod*a2%mod)%mod+(c2%mod*a4%mod)%mod)%mod
    c=((c3%mod*a1%mod)%mod+(c4%mod*a3%mod)%mod)%mod
    d=((c3%mod*a2%mod)%mod+(c4%mod*a4%mod)%mod)%mod
    return [[a,b],[c,d]]
def fast_matrix(l,p):
    if p==1:
        return l
    z=fast_matrix(l,p//2)
    if p%2==0:
        return mul(z,z)
    else:
        return mul(mul(z,z),l)
t=int(input())
for i in range(t):
    l=[[2,1],[2,0]]
    yo=[[1,3]]
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(3)
    else:
        z=fast_matrix(l,n-2)
        c1=z[0][0]
        c3=z[0][1]
        c2=z[1][0]
        c4=z[1][1]
        print((3*c1+c2)%mod)