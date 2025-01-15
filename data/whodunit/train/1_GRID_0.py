T=int(input())
for i in range(T):
    N=int(input())
    A=list()
    for j in range(N):
        A.append(input())
    B=['.'*N]*N
    C=['.'*N]*N
    for k in range(N):
        for l in range(N-1,-1,-1):
            if A[k][l]=='#':
                B[k]='#'*(l+1)+"."*(N-1-l)
                break
        for m in range(N-1,-1,-1):
            if A[m][k]=='#':
                C[k]='#'*(m+1)+'.'*(N-1-m)
                break
    sum=0
    for u in range(N):
        for v in range(N):
            if B[u][v]==C[v][u]=='.':
                sum+=1
    print(sum)
