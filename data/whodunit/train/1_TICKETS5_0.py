n=int(input())
while n>0:
    n-=1
    r=input()
    l=len(r)
    x=r[0]
    y=r[1]
    flag=1
    if x!=y:
        for i in range(l):
            if i%2==0 and r[i]==x:
                flag=1
            elif i&1 and r[i]==y:
                flag=1
            else:
                flag=0
                break
    else:
        flag=0
    if flag==1:
        print("YES")
    else:
        print("NO")