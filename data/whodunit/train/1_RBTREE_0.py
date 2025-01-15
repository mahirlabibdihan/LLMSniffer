from math import *
flag=0
for _ in range(int(input())):
    
    s=input().strip()
    if s=="Qi":
        flag=not flag
        continue
    (s,x,y)=s.split()
    (x,y)=(int(x),int(y))
    l1=[]
    l2=[]
    i=j=0
    l1.append(x)
    l2.append(y)
    while x>0:
        l1.append(x//2)
        x//=2
        i+=1
    while y>0:
        l2.append(y//2)
        y//=2
        j+=1
    while i>=0 and j>=0 and  l1[i]==l2[j]:
        (j,i)=(j-1,i-1)
    (j,i)=(j+1,i+1)
    ans=0
    if (i+1)%2==0:
        ans+=(i+1)//2
    else:
        ans+=(i//2)
        lo=int(log(l1[i],2))
        if s=="Qr":
            if flag + lo%2==1:
                ans+=1
        if s=="Qb":
            if (flag+ lo%2)%2==0:
                ans+=1
    j-=1
    if (j+1)%2==0:
        ans+=(j+1)//2
    else:
        ans+=(j//2)
        lo=int(log(l2[j],2))
        if s=="Qr":
            if flag + lo%2==1:
                ans+=1
        if s=="Qb":
            if (flag+ lo%2)%2==0:
                ans+=1
    print(ans)