import bisect
T=int(input())
for i in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    b=set(A)
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        if (x+y) in b:
            print(-1)
        else:
            print(bisect.bisect_right(A,x+y))
        
        