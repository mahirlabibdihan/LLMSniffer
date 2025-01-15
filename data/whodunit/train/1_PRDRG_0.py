a=list(map(int,input().split()))
l=[]
for i in range (a[0]):
    x=((2**a[i+1])-((-1)**a[i+1]))//3
    y=2**a[i+1]
    l.append(x)
    l.append(y)
for i in range (len(l)):
    print(l[i], end=" ")