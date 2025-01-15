n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    s=[]
    for i in range(m):
        a=list(map(int,input().split()))
        s.extend(a)
    s.sort()
    c=[]
    g=[]
    for i in range(len(s)):
        if(i%2==0):
            c.append(s[-1-i])
        else:
            g.append(s[-1-i])
    if sum(c)>sum(g):
        print("Cyborg")
    elif(sum(c)==sum(g)):
        print("Draw")
    else:
        print("Geno")