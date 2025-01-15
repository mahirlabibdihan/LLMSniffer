from sys import stdin, stdout
def fun(a,k):
    for i in range(len(a)):
        if a[i]==k:yield i
def ind(a,k,s,e):
    for i in range(s,e):
        if a[i]<k:return i
    return e
def rind(a,k,e,s):
    for i in range(e-1,s-1,-1):
        if a[i] <= k: return i
    return -1
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
q = int(stdin.readline())
for i in range(q):
    m = int(stdin.readline())
    b=tuple(fun(a,m))
    ans=0
    for i in range(len(b)):
        if b[i]==0:
            k=ind(a,a[b[i]],b[i]+1,n)
            ans+=k-b[i]
        elif b[i]==n-1:
            k=rind(a,a[b[i]],b[i],0)
            ans+=b[i]-k
        else:
            ans+=(b[i]-rind(a,a[b[i]],b[i],0))*(ind(a,a[b[i]],b[i]+1,n)-b[i])
    stdout.write(str(ans) + '\n')