def dt(n):
    if n<10:
        return n
    else:
        e=str(n)
        n=0
        for i in e:
            n+=int(i)
        return dt(n)
def lis(a,d):
    l=[]
    for i in range(9):
        l.append(dt(a+i*d))
    return l 
def rs(l,r):
    s=r//9
    w=r%9
    ans=0 
    for i in range(w):
        ans+=l[i]
    ans+=sum(l)*s
    return ans
for i in range(int(input())):
    a,d,l,r=map(int,input().split())
    w=lis(a,d)
    
    print(rs(w,r)-rs(w,l-1))