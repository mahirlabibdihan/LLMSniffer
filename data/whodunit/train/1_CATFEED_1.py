def chk(a,k,n):
    for i in range(1,k):
        if a[i] in a[:i] and a[:i].count(a[i])>i//n:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:k]))
    print(chk(a,k,n))
        