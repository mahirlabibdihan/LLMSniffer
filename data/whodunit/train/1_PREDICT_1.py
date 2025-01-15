def money(p,c=10000):
    p=max(p,1-p)
    x=p*(3-2*p)
    return(c*x)
t=int(input())
for i in range(t):
    p=float(input())
    print(money(p))
