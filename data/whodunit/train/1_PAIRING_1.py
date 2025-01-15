T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    l=[]
    q=[]
    p=[]
    for i in range(m):
        k,x=map(int,input().split())
        l.append([k,x])
    for i in reversed(range(m)):
        if l[i][0] not in q and l[i][1] not in q:
            q.append(l[i][0])
            q.append(l[i][1])
            p.append(i)
    p.sort()
    for i in range(len(p)):
        print(p[i],end=' ')
    print()