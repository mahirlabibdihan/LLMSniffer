n,m=map(int, input().split())
for i in range(m):
    q=int(input())
    
    if q<n+2 or q>3*n:
        print(0)
    elif q<2*n+1:
        print(q-n-1)
    else:
        print(3*n-q+1)