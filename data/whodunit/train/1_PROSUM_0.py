T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))[:N]
    c=(N*(N-1))//2
    b=A.count(1)+A.count(0)
    d=A.count(2)
    c=c-((b*(b-1))//2)-b*(N-b)-((d*(d-1))//2)
    print(c)