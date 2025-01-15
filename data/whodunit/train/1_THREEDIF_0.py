T=int(input())
mod=1000000007
for k in range(T):
    A,B,C=map(int,input().split())
    q=[A,B,C]
    q.sort()
    c=q[0]*(q[1]-1)*(q[2]-2)
    print(c%mod)