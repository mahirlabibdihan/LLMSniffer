di={}
li=[]
lis=[]
    
for i in range(int(input())):
    s,n=map(str,input().split())
    di[n]=s
    li.append(int(n))
li.sort(reverse=True)
for i in li:
    lis.append(di[str(i)])
for i in range(int(input())):
    q=input()
    for j in range(len(lis)):
        if q in lis[j] and q==lis[j][0:len(q)]:
            print(lis[j])
            break
            
    else:
        print('NO')
    
    