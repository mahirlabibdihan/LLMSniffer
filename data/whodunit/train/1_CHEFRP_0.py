for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(len(l)):
        if l[i]<2:
            flag=1
            break
    if flag==1:
        print(-1)
        continue
    s=sum(l)-min(l)+2
    if len(l)==1:
        print(2)
    else:
        print(s)