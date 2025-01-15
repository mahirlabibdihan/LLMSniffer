T=int(input())
mod=(10**9)+7
for _ in range(T):

    N=int(input())

    A=list(map(int,input().split()))[:N]

    B={}

    for i in range(N):
        B[A[i]]=i
    
    newresult=[0]*N
    A.sort()
    for i in range(N):

        index=B[A[i]]
        value = ((pow(2,i,mod)-1) + ((pow(2,i,mod)*(N-i-1))%mod) + ((pow(2,i,mod)*((N-i-1)*(N-i-2))//2)%mod))%mod
        newresult[index]=value
    
    print(*newresult)
