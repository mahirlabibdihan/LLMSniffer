for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    
    l.sort()
    d=[]
    for i in l:
        d.append(l.count(i))
    maxc=max(d)
    for i in l:
        if l.count(i)==maxc:
            print(i,maxc)
            break
