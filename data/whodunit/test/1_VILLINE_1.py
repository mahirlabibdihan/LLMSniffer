ll=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(ll):
    x=list(map(int,input().split()))
    if l[0]*x[0]+l[1]-x[1]>0:
            c=c+x[2]
    elif l[0]*x[0]+l[1]-x[1]<0:
            c1=c1+x[2]
if c>c1:
        print(c)
else:
        print(c1)