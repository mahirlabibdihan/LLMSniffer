for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=10000000000
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])<m:
            m=abs(l[i]-l[i+1])
    print(m)
            