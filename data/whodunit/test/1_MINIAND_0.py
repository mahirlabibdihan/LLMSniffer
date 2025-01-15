t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    oddcount = [0 for i in range(n+1)]
    for i in range(n):
        if a[i]%2==1: oddcount[i+1]=oddcount[i]+1
        else: oddcount[i+1] = oddcount[i]
    q = int(input())
    for _ in range(q):
        (l,r) = map(int,input().split())
        if oddcount[r]-oddcount[l-1]==r-l+1: print("ODD")
        else: print("EVEN")