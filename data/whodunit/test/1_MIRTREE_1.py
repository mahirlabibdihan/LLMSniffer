n,q=list(map(int, (input().split(' '))))
ans=1000000007
leaves=2**n
edges=((2**(n+1))-2)%ans
height=n+1
op=[]
root=1
for i in range(q):
    s=str(input())
    if s[0]=="2":
        op.append("disp")
    else:
        k=list(map(int,s.split()))
        op.append(k[1])
for j in op:
    if j=="disp":
        print(edges)
    elif j==1 or j==2:
        edges=(2*edges+height)%ans
        leaves=(2*leaves)%ans
        root=(root*2)%ans
    elif j==4:
        edges=(2*edges+leaves)%ans
        leaves=(root)
        height=(2*height)%ans
    else:
        edges=(2*edges+root)%ans
        root=leaves
        height=(2*height)%ans
