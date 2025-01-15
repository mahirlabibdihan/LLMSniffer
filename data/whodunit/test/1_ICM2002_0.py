x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    print('YES' if s%b==0 and s/b>=max(l) else 'NO')