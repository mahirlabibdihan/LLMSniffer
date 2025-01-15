def pow_mod(base,exp,N):
    result=1
    while exp>0:
        if exp%2==1:
            result=(result*base)%N
        exp=exp>>1
        base=(base*base)%N
    return result


N=1000000007
t=int(input())
for i in range(t):
    [n,m,d,k]=input().split(" ")
    n=int(n)
    m=int(m)
    d=int(d)
    k=int(k)
    if m>d:
        t1=m-d
        t2=pow_mod(d+1,n,N)
        t3=pow_mod(d,n,N)
        t4=pow_mod(d-1,n,N)
        ans=((t2-2*t3+t4)*t1)%N
        print(ans)
    else:
        print("0")
        