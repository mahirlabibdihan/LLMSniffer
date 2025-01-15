def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
def solve(a,n,m):
    
    return a; 
for tastcas in range(int(input())):
    n,m=li(); a=[li() for i in range(n)]; f=0; 
    for i in range(n):
        for j in range(m):
            if(a[i][j]!=-1 and ((i>0 and a[i-1][j]>a[i][j]) or (j>0 and a[i][j-1]>a[i][j]))): f=1; break; 
            elif(a[i][j]==-1):
                t=1
                if(i>0): t=max(t,a[i-1][j]); 
                if(j>0): t=max(t,a[i][j-1]); 
                a[i][j]=t; 
        if(f==1): break; 
    if(f==1): print(-1)
    else:
        for i in range(n):
            for j in range(m):
                print(a[i][j],end=' ')
            print()