n=int(input())
z=[]
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    z.append(a)
x,y=[],[]
e=max(z)
f=min(z)
for i in range(len(z)):
    if(z[i]==e):
        x.append(i+1)
    if(z[i]==f):
        y.append(i+1)
print(y[-1],x[-1])