
n,q=map(int,input().split())
nli=[0]+list(map(int,input().split()))
d=[0]
for i in range(1,n+1):
    d.append(d[i-1]^nli[i])

for j in range(q):
    qi=int(input())
    print(d[qi%(n+1)])