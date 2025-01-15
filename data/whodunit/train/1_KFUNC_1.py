def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
def reduceTo1(n):
    if(len(str(n))==1): return n; 
    else:
        sum=0; 
        for i in str(n): sum+=int(i); 
        return reduceTo1(sum); 
for tastcas in range(int(input())):
    a1,d,l,r=li(); al=a1+(l-1)*d; nos=[reduceTo1(al)]; 
    t=reduceTo1(nos[-1]+d); 
    while(t!=nos[0]):nos.append(t); t=reduceTo1(nos[-1]+d); 
    length=len(nos); rng=r-l+1; s1=rng//length; ans=s1*sum(nos); 
    for i in range(rng-s1*length): ans+=nos[i]; 
    print(ans)