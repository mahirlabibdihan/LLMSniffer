t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    a=[]
    a.append(sum(l))
    a.append(sum(m))
    a.append(sum(n))
    a.append(l[0]+m[0]+n[0])
    a.append(l[1]+m[1]+n[1])
    a.append(l[2]+m[2]+n[2])
    c=max(a)
    if c>0:
        if c%2==0:
            print(c-1)
        else:    
            print(c)    
    else:
        print(0)