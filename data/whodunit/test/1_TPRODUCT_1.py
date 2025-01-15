def makeAdj(arr):
    n = len(arr)
    adj = {i : [] for i in range(n)}
    for i in range(n):
        if 2*i + 2 < n:
            adj[i].append(2*i+1)
            adj[i].append(2*i+2)
            adj[2*i+1].append(i)
            adj[2*i+2].append(i)
        elif 2*i + 1 < n:
            adj[i].append(2*i+1)
            adj[2*i+1].append(i)
    return adj

def dfs(node,par,arr,adj,P):
    if len(adj[node]) == 1:
        P[node] = arr[node]
        return
    for child in adj[node]:
        if child == par:
            continue
        dfs(child,node,arr,adj,P)
        P[node] = max(P[child]*arr[node],P[node])
    return P

while True:
    h = int(input())
    if h == 0:
        break
    arr = list(map(int,input().split()))
    adj = makeAdj(arr)
    P = [0]*(len(arr))
    print(dfs(0,-1,arr,adj,P)[0] % 1000000007)
    # print(P[0])
    


    
