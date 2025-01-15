for _ in range(int(input())):    
    a,b,out = map(int,input().split());r=10**2+5
    d,s = [0]*(10**5),[0]*r   
    for i in range(r):       
        for j in range(r):d[i*r+j]=1 if (i==j or j==0) else d[(i-1)*r+j-1]+d[(i-1)*r+j]
    for i in range(b+1):        
        ans=pow(a+1,i+1)-1       
        for j in range(i):ans-=d[(i+1)*r+j]*s[j];
        s[i]=ans//(i+1)
    print(s[b]%out)