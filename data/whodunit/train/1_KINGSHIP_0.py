t=int(input())
for k in range(t):
    n=int(input())
    p=list(map(int, input().split()))[:n]
    x=min(p)
    sum=0
    for i in p:
        y=i*x
        sum=sum+y
    new_sum=sum-(x*x)
    print(new_sum)
        
    