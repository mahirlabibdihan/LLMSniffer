for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l1=[]
    for j in range(n):
        if a[j]%2==0:l1.append(j+1)
    q=int(input())
    for x in range(q):
        l,r=map(int,input().split())
        for e in l1:
            if e>=l and e<=r:
                print('EVEN')
                break
        else:print('ODD')