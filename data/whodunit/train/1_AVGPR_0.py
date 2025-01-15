
def ti(): return tuple(map(int,input().split())); 
def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
for tastcas in range(int(input())):
    n=ii(); a=li(); d={}; ans=0; 
    for i in range(-1000,1001): d[i]=0;
    for i in a: d[i]+=1; 
    for i in range(-1000,1001):
        for j in range(i,1001,2):
            if(i==j):
                x=(i+j)/2; 
                if(d[x]): ans+=(d[i]*(d[i]-1))//2; 
            else:
                x=(i+j)//2; 
                if(d[x]): ans+=(d[i]*d[j]); 
    print(ans); 