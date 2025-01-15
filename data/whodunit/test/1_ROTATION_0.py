x,y=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(y):
    p,q=input().split()
    q=int(q)
    if p=="C":
        count+=q
    elif p=="A":
        count-=q
    else:
        print(a[(q-1+count)%x])