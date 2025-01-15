def capimove(edges,wts,wts_dict):
    for e in wts:
        if wts_dict[e] not in edges:
            return wts_dict[e]
    return 0

t=int(input())

for i in range(t):
    n=int(input())
    wts = [0]+[int(i) for i in input().split()]
    wts_dict = {wts[i]:i for i in range(1,n+1)}
    wts.sort(reverse=True)
    adj = {i:[i] for i in range(1,n+1)}
    for _ in range(n-1):
        i,j=map(int,input().split())
        adj[i].append(j)
        adj[j].append(i)
    for k in range(1,n+1):
        print(capimove(adj[k],wts,wts_dict),end=" ")
    print()