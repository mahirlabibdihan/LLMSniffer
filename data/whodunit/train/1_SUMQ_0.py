t=int(input())
for _ in range(t):
    p,q,r=map(int,input().split()) 
    a1=sorted(list(map(int,input().split())))
    a2=sorted(list(map(int,input().split())))
    a3=sorted(list(map(int,input().split()))) 
    a=b=c=d=0
    n=0
    mod = 10 ** 9 + 7 
    for i in a2:
        while a<p and a1[a]<=i:
            c+=a1[a] 
            a+=1 
        while b<r and a3[b]<=i:
            d+=a3[b] 
            b+=1 
        n+=(i*a+c)*(i*b+d)
        n%=mod
    print(n)        
            