for t in range(int(input())):
    N=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l1=[]
    for i in range(N-1):
        l1.append(l[i+1]-l[i])
    print(min(l1))
