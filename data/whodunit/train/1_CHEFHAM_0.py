

for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(n):
        a.append([li[i],i])
        b.append(li[i])
    
    a.sort()
    b.sort(reverse=True)
    flag = False
   
    for i in range(n):
       if b[i]==a[i][0]:
           if flag==False:
               b[i],b[0]=b[0],b[i]
               flag = True
           else:
               b[i],b[n-1]=b[n-1],b[i]
    ct = 0
    co = [0]*n
    
    for i in range(n):
        if b[i] != a[i][0]:
            ct+=1
        co[a[i][1]]=b[i]
    print(ct)
    print(*co)