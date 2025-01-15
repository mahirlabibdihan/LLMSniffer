T=int(input())

for k in range(T):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    L.sort()
    m=max(L)
    for i in range(K):
        L.append(m)
        m+=1

    print(L[len(L)//2])