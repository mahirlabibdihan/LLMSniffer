t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c=[0]*m
    for i in range(n):
        x=input()
        for k in range(m):
            if x[k]=='1':
                c[k]+=1
    sum1=0
    for i in range(m):
        if c[i]>1:
            sum1+=(c[i]*(c[i]-1)//2)
    print(sum1)