import itertools
T=int(input())
for i in range(T):
    l=[]
    a,b=map(int,input().split())
    for j in range(a):
        n=int(input())
        l.append(n)
    q=[]
    for k in range(len(l)+1):
        for j in itertools.combinations(l,k):
            if(sum(j)==b):
                q.append(sum(j))
    if(len(q)!=0):
        print('Yes')
    else:
        print('No')
            
    