t=int(input())
while t!=0:
    s=input()
    s+='X'
    n=len(s)
    m1=m2=c1=c2=0
    for i in range(0,n-1):
        if s[i]!=s[i+1]:
            if s[i]=='U':
                c1+=1
            if s[i]=='D':
                c2+=1
            if m1<c1 :
                m1=c1
            if m2<c2 :
                m2=c2;
    if m1>m2:
        d=m2
    else:
        d=m1
    print(d)
    t-=1