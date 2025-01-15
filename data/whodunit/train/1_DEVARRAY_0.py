n,k=map(int,input().split())
n=list(map(int,input().split()))
a=max(n)
b=min(n)
for i in range(k):
    p=int(input())
    if p<b or p>a:
        print("No")
    else:
        print("Yes")