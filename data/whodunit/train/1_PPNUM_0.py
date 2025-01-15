def li(): return list(map(int,input().split())); return a; 
def si(): return input().split()
def ii(): return int(input())
highs={i: 10**(i-1) for i in range(12)}; 
lows={i: 10**(i) for i in range(12)}; 
inf=1000000007; 
for tastcas in range(int(input())):
    l,r=si(); ll=len(l); rl=len(r); l=int(l); r=int(r); 
    if(ll==rl): ans=(((l+r)*(r-l+1))*ll)//2; 
    else:
        r1=(10**ll)-1; r2=10**(rl-1); 
        ans = ( ((((l+r1)*(r1-l+1))*ll)//2) + ((((r2+r)*(r-r2+1))*rl)//2) ) % inf; 
        for i in range(ll+1,rl):
            a=10**(i-1); b=(10**i)-1; 
            ans += ((((a+b)*(b-a+1))*i)//2); 
            ans%=inf; 
    print(ans%inf); 