e=10**7+7
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ans=1
for i in range(m):
    c=0
    for j in range(n):
        c+=l[j][i]
    ans=(ans*c)%e
print(ans)