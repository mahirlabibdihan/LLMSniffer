t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int, input().split()))
    a=[]
    b=0
    for i in range(n):
        for j in range(i+1,n):
            b=li[i]+li[j]
            a.append(b)
    max_count=max(a)
    c=a.count(max_count)
    print("%.8f"% (c/len(a)))