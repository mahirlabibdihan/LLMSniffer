for x in range(int(input())):
    a=[]
    b=[]
    c=int(input())
    for i in range(c):
        d,e=map(str,input().split(' '))
        a.append(d)
        b.append(int(e))
    f=set(b)
    m=1
    for j in range(len(f)):
        g=min(f)
        if b.count(g)==1:
            k=b.index(g)
            m=2
            print(a[k])
            break
        else:
            f.remove(g)
    if m==1:
        print("Nobody wins.")