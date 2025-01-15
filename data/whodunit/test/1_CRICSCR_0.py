n=int(input())
fg=0
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
for i in range(1,n):
    if l[i][0]<l[i-1][0]:
        fg=1
        break
    elif l[i-1][1]>l[i][1]:
        fg=1
        break
    elif l[i-1][1]==10 and l[i][1]==10 and l[i-1][0]!=l[i][0]:
        fg=1
        break
if fg==0:
    print("YES")
else:
    print("NO")