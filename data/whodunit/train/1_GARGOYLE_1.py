def dec(x):
    x=x[::-1];c=0
    #print(x)
    for i in range(len(x)):
        if x[i]=='T':
            c+=pow(2,i)
    return c
a=[]
for _ in range(int(input())):
    a.append(input().split())
#print(a)
b=[];m=0
for i in a:
    x=''.join(i)
    b.append(dec(x))
for i in range(len(a)):
    g=b[i];c=1;k=0
    for j in range(len(a)):
        if a[i][j]=='T' and i!=j:
            k+=1
        if a[i][j]=='T' and b[j]==g and i!=j:
            c+=1
    if k+1==c:    
        m=max(m,c)
        
print(m)
