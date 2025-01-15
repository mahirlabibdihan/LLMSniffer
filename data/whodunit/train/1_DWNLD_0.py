t=int(input())
for l in range(t):
    n,k=map(int,input().split())
    minute=[]
    mb_per_minute=[]
    for i in range(n):
        a,b=map(int,input().split(' '))
        minute.append(a)
        mb_per_minute.append(b)
    i=0
    while(k>0 and i<n):
        if(minute[i]>=k):
            minute[i]=minute[i]-k
            k=0
        elif(minute[i]<k):
            k=k-minute[i]
            minute[i]=0
            
        if(minute[i]==0):
            minute.pop(i)
            mb_per_minute.pop(i)
    
    #print(minute)
#    print(mb_per_minute)
    sum=0
    for i in range(len(minute)):
        sum+=minute[i]*mb_per_minute[i]
    print(sum)