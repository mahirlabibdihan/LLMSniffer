for _ in range(int(input())):
    n=int(input())
    s=input()
    l=list(map(int,input().split()))
    a=0
    if n==1:
        print(0)
        continue
    for i in range(1,n):
        a+=l[i]-l[i-1]
    flag=0
    t=[]
    d=[]
    for i in range(n):
        if s[i]=='1':
            if flag==0:
                flag=1 
                continue
            d.append(l[i]-l[i-1])
            t.append(d)
            d=[]
        else:
            if flag==0:
                continue
            d.append(l[i]-l[i-1])
    for i in t:
        a-=max(i)
    print(a)
            