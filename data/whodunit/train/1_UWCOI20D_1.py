t=int(input())
while t>0:
    n=int(input())
    l=[]
    l.append(0)
    for i in range(1,n+1):
        c=input()
        for j in range(n):
            if c[j]=='1': 
                l.append(j+1)
    sum1=0
    for j in range(1,n+1):
        min1=l[j]
        max1=l[j]
        for k in range(j,n+1):
            min1=min(min1,l[k])
            max1=max(max1,l[k])
            if max1-min1==k-j:
                sum1+=1
    print(sum1)
    t-=1
                
            
                