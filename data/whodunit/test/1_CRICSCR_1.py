n=int(input())
r=[]
w=[]
for i in range(n):
    a,b=map(int,input().split())
    r.append(a)
    w.append(b)
    
ans=0
if n==1 and w[i]<=10:
    print("YES")
else:
    for i in range(n-1):
        if(r[i]<=r[i+1] and w[i]<=w[i+1]):
            if(w[i]==10 and w[i]==w[i+1]):
                ans=0
            else:
                ans=1
        else:
            ans=0
            break
    if ans==0:
        print("NO")
    else:
        print("YES")