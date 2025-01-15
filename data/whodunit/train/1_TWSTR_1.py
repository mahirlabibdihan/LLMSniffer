n=int(input())
a=[]
b=[]
for _ in range(n):
    s=input().split()
    a.append(s[0])
    b.append(int(s[1]))
    

q=int(input())
for i in range(q):
    x=input()
    
    m=-(10**10)
    for k in range(n):
        y=a[k]
        if(x in y and x==y[0:len(x)]):
            m=max(m,b[k])
            
    if(m==-(10**10)):
        print("NO")
    else:
        j=b.index(m)
        print(a[j])
    